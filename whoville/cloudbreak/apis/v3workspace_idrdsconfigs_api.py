# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class V3workspaceIdrdsconfigsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_rds_config_in_workspace(self, workspace_id, **kwargs):
        """
        create RDS config in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_rds_config_in_workspace(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param RdsConfig body:
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_rds_config_in_workspace_with_http_info(workspace_id, **kwargs)
        else:
            (data) = self.create_rds_config_in_workspace_with_http_info(workspace_id, **kwargs)
            return data

    def create_rds_config_in_workspace_with_http_info(self, workspace_id, **kwargs):
        """
        create RDS config in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_rds_config_in_workspace_with_http_info(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param RdsConfig body:
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_rds_config_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `create_rds_config_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RDSConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_rds_config_in_workspace(self, workspace_id, name, **kwargs):
        """
        delete RDS config by name in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_rds_config_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_rds_config_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.delete_rds_config_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def delete_rds_config_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        delete RDS config by name in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_rds_config_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_rds_config_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `delete_rds_config_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_rds_config_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs/{name}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RDSConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_rds_config_in_workspace(self, workspace_id, name, **kwargs):
        """
        get RDS config by name in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_rds_config_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_rds_config_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.get_rds_config_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def get_rds_config_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        get RDS config by name in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_rds_config_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RDSConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rds_config_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_rds_config_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_rds_config_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RDSConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_rds_request_from_name_in_workspace(self, workspace_id, name, **kwargs):
        """
        get request in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_rds_request_from_name_in_workspace(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RdsConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_rds_request_from_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
        else:
            (data) = self.get_rds_request_from_name_in_workspace_with_http_info(workspace_id, name, **kwargs)
            return data

    def get_rds_request_from_name_in_workspace_with_http_info(self, workspace_id, name, **kwargs):
        """
        get request in workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_rds_request_from_name_in_workspace_with_http_info(workspace_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str name: (required)
        :return: RdsConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rds_request_from_name_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_rds_request_from_name_in_workspace`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_rds_request_from_name_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs/{name}/request', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RdsConfig',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_rds_configs_by_workspace(self, workspace_id, **kwargs):
        """
        list RDS configs for the given workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_rds_configs_by_workspace(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :return: list[RDSConfigResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_rds_configs_by_workspace_with_http_info(workspace_id, **kwargs)
        else:
            (data) = self.list_rds_configs_by_workspace_with_http_info(workspace_id, **kwargs)
            return data

    def list_rds_configs_by_workspace_with_http_info(self, workspace_id, **kwargs):
        """
        list RDS configs for the given workspace
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_rds_configs_by_workspace_with_http_info(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :return: list[RDSConfigResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_rds_configs_by_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `list_rds_configs_by_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[RDSConfigResponse]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def test_rds_connection_in_workspace(self, workspace_id, **kwargs):
        """
        test RDS connectivity
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_rds_connection_in_workspace(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param RdsTestRequest body:
        :return: RdsTestResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_rds_connection_in_workspace_with_http_info(workspace_id, **kwargs)
        else:
            (data) = self.test_rds_connection_in_workspace_with_http_info(workspace_id, **kwargs)
            return data

    def test_rds_connection_in_workspace_with_http_info(self, workspace_id, **kwargs):
        """
        test RDS connectivity
        An RDS Configuration describe a connection to an external Relational Database Service that can be used as the Hive Metastore.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_rds_connection_in_workspace_with_http_info(workspace_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param RdsTestRequest body:
        :return: RdsTestResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_rds_connection_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `test_rds_connection_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/rdsconfigs/testconnect', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RdsTestResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
