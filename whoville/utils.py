#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convenience utility functions for whoville, not really intended for external use
"""

from __future__ import absolute_import, unicode_literals
import logging
import json
import time
import base64
import six
from six.moves import reduce
import os
import ruamel.yaml
import requests
from github import Github
from requests.models import Response
from whoville import config

__all__ = ['dump', 'load', 'fs_read', 'fs_write', 'wait_to_complete',
           'is_endpoint_up', 'set_endpoint', 'get_val',
           'load_resources_from_files', 'load_resources_from_github']

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def dump(obj, mode='json'):
    """
    Dumps a native datatype object to json or yaml, defaults to json

    Args:
        obj (varies): The native datatype object to serialise
        mode (str): 'json' or 'yaml', the supported export modes

    Returns (str): The serialised object

    """
    assert mode in ['json', 'yaml']
    try:
        out = json.dumps(
            obj=obj,
            sort_keys=True,
            indent=4
            # default=_json_default
        )
    except TypeError as e:
        raise e
    if mode == 'json':
        return out
    if mode == 'yaml':
        return ruamel.yaml.safe_dump(
            json.loads(out),
            default_flow_style=False
        )
    raise ValueError("Invalid dump Mode specified {0}".format(mode))


def load(obj, dto=None, decode=None):
    """
    Loads a serialised object back into native datatypes, and optionally
    imports it back into the native NiFi DTO

    Warning: Using this on objects not produced by this Package may have
    unintended results! While efforts have been made to ensure that unsafe
    loading is not possible, no stringent security testing has been completed.

    Args:
        obj (dict, list): The serialised object to import
        dto (Optional [tuple{str, str}]): A Tuple describing the service and
        object that should be constructed.

        e.g. dto = ('registry', 'VersionedFlowSnapshot')

    Returns: Either the loaded object in native Python datatypes, or the
        constructed native datatype object

    """
    assert isinstance(obj, (six.string_types, bytes))
    assert dto is None or isinstance(dto, tuple)
    assert decode is None or isinstance(decode, six.string_types)
    # ensure object is standard json before reusing the api_client deserializer
    # safe_load from ruamel.yaml as it doesn't accidentally convert str
    # to unicode in py2. It also manages both json and yaml equally well
    # Good explanation: https://stackoverflow.com/a/16373377/4717963
    # Safe Load also helps prevent code injection
    if decode:
        if decode == 'base64':
            prep_obj = base64.b64decode(obj)
        else:
            raise ValueError("Load's decode option only supports base64")
    else:
        prep_obj = obj
    loaded_obj = ruamel.yaml.safe_load(prep_obj)
    if dto:
        assert dto[0] in ['cloudbreak']
        assert isinstance(dto[1], six.string_types)
        obj_as_json = dump(loaded_obj)
        response = Response()
        response.data = obj_as_json
        api_clients = {
            'cloudbreak': config.cb_config.api_client,
        }
        api_client = api_clients[dto[0]]
        return api_client.deserialize(
            response=response,
            response_type=dto[1]
        )
    return loaded_obj


def fs_write(obj, file_path):
    """
    Convenience function to write an Object to a FilePath

    Args:
        obj (varies): The Object to write out
        file_path (str): The Full path including filename to write to

    Returns: The object that was written
    """
    try:
        with open(str(file_path), 'w') as f:
            f.write(obj)
        return obj
    except TypeError as e:
        raise e


def fs_read(file_path):
    """
    Convenience function to read an Object from a FilePath

    Args:
        file_path (str): The Full path including filename to read from

    Returns: The object that was read
    """
    try:
        with open(str(file_path), 'r') as f:
            return f.read()
    except IOError as e:
        raise e


def wait_to_complete(test_function, *args, **kwargs):
    """
    Implements a basic return loop for a given function which is capable of a
    True|False output

    Args:
        test_function: Function which returns a bool once the target
            state is reached
        delay (int): The number of seconds between each attempt, defaults to
            config.short_retry_delay
        max_wait (int): the maximum number of seconds before issuing a Timeout,
            defaults to config.short_max_wait
        *args: Any args to pass through to the test function
        **kwargs: Any Keyword Args to pass through to the test function

    Returns (bool): True for success, False for not

    """
    log.info("Called wait_to_complete for function %s",
             test_function.__name__)
    delay = kwargs.pop('whoville_delay', config.short_retry_delay)
    max_wait = kwargs.pop('whoville_max_wait', config.short_max_wait)
    timeout = time.time() + max_wait
    while time.time() < timeout:
        log.debug("Calling test_function")
        test_result = test_function(*args, **kwargs)
        log.debug("Checking result")
        if test_result:
            log.info("Function output [%s] eval to True, returning output",
                     str(test_result)[:25])
            return test_result
        log.info("Function output [%s] evaluated to False, sleeping...",
                 str(test_result)[:25])
        time.sleep(delay)
    log.info("Hit Timeout, raising TimeOut Error")
    raise ValueError("Timed Out waiting for {0} to complete".format(
        test_function.__name__))


def is_endpoint_up(endpoint_url, verify=False):
    """
    Tests if a URL is available for requests

    Args:
        endpoint_url (str): The URL to test
        verify (bool): Whether to attempt SSL verification, if SSL needed

    Returns (bool): True for a 200 response, False for not

    """
    log.info("Called is_endpoint_up with args %s", locals())
    try:
        response = requests.get(endpoint_url, verify=verify)
        if response.status_code == 200:
            log.info("Got 200 response from endpoint, returning True")
            return True
        log.info("Got status code %s from endpoint, returning False",
                 response.status_code)
        return False
    except requests.ConnectionError:
        log.info("Got ConnectionError, returning False")
        return False


def set_endpoint(endpoint_url):
    """
    EXPERIMENTAL

    Sets the endpoint when switching between instances of NiFi or other
    projects. Not tested extensively with secured instances.

    Args:
        endpoint_url (str): The URL to set as the endpoint. Autodetects the
        relevant service e.g. 'http://localhost:18080/nifi-registry-api'

    Returns (bool): True for success, False for not
    """
    log.info("Called set_endpoint with args %s", locals())
    if 'cb/api' in endpoint_url:
        log.info("Setting Cloudbreak endpoint to %s", endpoint_url)
        this_config = config.cb_config
    else:
        raise ValueError("Unrecognised API Endpoint")
    if this_config.api_client:
        this_config.api_client.host = endpoint_url
    this_config.host = endpoint_url
    if this_config.host == endpoint_url:
        return True
    return False


# https://stackoverflow.com/a/14692747/4717963
def get_val(root, items, sep='.'):
    """
    Swagger client objects don't behave like dicts, so need a custom func
    to step down through keys when defined as string vars etc.

    Warnings:
        If you try to retrieve a key that doens't exist you will get None
        instead of an Attribute Error. Code defensively.

    Args:
        root [dict, client obj]: The dict or Object to recurse through
        items (list, str): either list or dot notation string of keys to walk
            through
        sep (str): The character expected as a separator when parsing strings

    Returns (varies): The target val at the last key

    """
    assert isinstance(items, (list, six.string_types))
    for i in items if isinstance(items, list) else items.split(sep):
        if isinstance(root, dict):
            root = root.get(i)
        else:
            root = root.__getattribute__(i)
    return root


def load_resources_from_github(repo_name, username, token, tgt_dir, ref='master',
                    recurse=True):

    def _recurse_github_dir(g_repo, r_tgt, r_ref):
        contents = g_repo.get_dir_contents(r_tgt, r_ref)
        out = {}
        for obj in contents:
            if obj.type == 'dir':
                out[obj.name] = _recurse_github_dir(g_repo, obj.path, r_ref)
            elif obj.type == 'file':
                if obj.name.rsplit('.')[1] not in ['yaml', 'json']:
                    out[obj.name] = obj.decoded_content
                else:
                    # Valid yaml can't have tabs, only spaces
                    # proactively replacing tabs as some tools do it wrong
                    out[obj.name] = load(obj.decoded_content)
        return out

    g_accnt = Github(username, token)
    g_repo = g_accnt.get_repo(repo_name)
    if not recurse:
        listing = g_repo.get_dir_contents(tgt_dir, ref)
        return listing
    return {'resources': _recurse_github_dir(g_repo, tgt_dir, ref) }


def load_resources_from_files(file_path):
    resources = {}
    # http://code.activestate.com/recipes/577879-create-a-nested-dictionary-from-oswalk/
    rootdir = file_path.rstrip(os.sep)
    head = rootdir.rsplit(os.sep)[-1]
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], resources)
        parent[folders[-1]] = subdir
        for file_name in subdir.keys():
            log.info("loading [%s]", os.path.join(path, file_name))
            if file_name.rsplit('.')[1] not in ['yaml', 'json']:
                subdir[file_name] = fs_read(os.path.join(path, file_name))
            else:
                # Valid yaml can't have tabs, only spaces
                # proactively replacing tabs as some tools do it wrong
                subdir[file_name] = load(
                    fs_read(os.path.join(
                        path, file_name
                    ))
                )
    return resources[head]


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton