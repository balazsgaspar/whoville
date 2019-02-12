# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestResponseDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status_code': 'int',
        'status_text': 'str',
        'media_type': 'str',
        'headers': 'dict(str, str)',
        'cookies': 'dict(str, str)',
        'body': 'str'
    }

    attribute_map = {
        'status_code': 'statusCode',
        'status_text': 'statusText',
        'media_type': 'mediaType',
        'headers': 'headers',
        'cookies': 'cookies',
        'body': 'body'
    }

    def __init__(self, status_code=None, status_text=None, media_type=None, headers=None, cookies=None, body=None):
        """
        RestResponseDetails - a model defined in Swagger
        """

        self._status_code = None
        self._status_text = None
        self._media_type = None
        self._headers = None
        self._cookies = None
        self._body = None

        if status_code is not None:
          self.status_code = status_code
        if status_text is not None:
          self.status_text = status_text
        if media_type is not None:
          self.media_type = media_type
        if headers is not None:
          self.headers = headers
        if cookies is not None:
          self.cookies = cookies
        if body is not None:
          self.body = body

    @property
    def status_code(self):
        """
        Gets the status_code of this RestResponseDetails.

        :return: The status_code of this RestResponseDetails.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this RestResponseDetails.

        :param status_code: The status_code of this RestResponseDetails.
        :type: int
        """

        self._status_code = status_code

    @property
    def status_text(self):
        """
        Gets the status_text of this RestResponseDetails.

        :return: The status_text of this RestResponseDetails.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """
        Sets the status_text of this RestResponseDetails.

        :param status_text: The status_text of this RestResponseDetails.
        :type: str
        """

        self._status_text = status_text

    @property
    def media_type(self):
        """
        Gets the media_type of this RestResponseDetails.

        :return: The media_type of this RestResponseDetails.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this RestResponseDetails.

        :param media_type: The media_type of this RestResponseDetails.
        :type: str
        """

        self._media_type = media_type

    @property
    def headers(self):
        """
        Gets the headers of this RestResponseDetails.

        :return: The headers of this RestResponseDetails.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this RestResponseDetails.

        :param headers: The headers of this RestResponseDetails.
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def cookies(self):
        """
        Gets the cookies of this RestResponseDetails.

        :return: The cookies of this RestResponseDetails.
        :rtype: dict(str, str)
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        """
        Sets the cookies of this RestResponseDetails.

        :param cookies: The cookies of this RestResponseDetails.
        :type: dict(str, str)
        """

        self._cookies = cookies

    @property
    def body(self):
        """
        Gets the body of this RestResponseDetails.

        :return: The body of this RestResponseDetails.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this RestResponseDetails.

        :param body: The body of this RestResponseDetails.
        :type: str
        """

        self._body = body

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RestResponseDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
