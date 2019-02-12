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


class UserWorkspacePermissionsJson(object):
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
        'permissions': 'list[str]',
        'user_name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'user_name': 'userName',
        'user_id': 'userId'
    }

    def __init__(self, permissions=None, user_name=None, user_id=None):
        """
        UserWorkspacePermissionsJson - a model defined in Swagger
        """

        self._permissions = None
        self._user_name = None
        self._user_id = None

        if permissions is not None:
          self.permissions = permissions
        if user_name is not None:
          self.user_name = user_name
        if user_id is not None:
          self.user_id = user_id

    @property
    def permissions(self):
        """
        Gets the permissions of this UserWorkspacePermissionsJson.

        :return: The permissions of this UserWorkspacePermissionsJson.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this UserWorkspacePermissionsJson.

        :param permissions: The permissions of this UserWorkspacePermissionsJson.
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def user_name(self):
        """
        Gets the user_name of this UserWorkspacePermissionsJson.

        :return: The user_name of this UserWorkspacePermissionsJson.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UserWorkspacePermissionsJson.

        :param user_name: The user_name of this UserWorkspacePermissionsJson.
        :type: str
        """

        self._user_name = user_name

    @property
    def user_id(self):
        """
        Gets the user_id of this UserWorkspacePermissionsJson.

        :return: The user_id of this UserWorkspacePermissionsJson.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserWorkspacePermissionsJson.

        :param user_id: The user_id of this UserWorkspacePermissionsJson.
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, UserWorkspacePermissionsJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
