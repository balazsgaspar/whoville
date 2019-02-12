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


class StackScaleRequestV2(object):
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
        'group': 'str',
        'desired_count': 'int'
    }

    attribute_map = {
        'group': 'group',
        'desired_count': 'desiredCount'
    }

    def __init__(self, group=None, desired_count=None):
        """
        StackScaleRequestV2 - a model defined in Swagger
        """

        self._group = None
        self._desired_count = None

        self.group = group
        self.desired_count = desired_count

    @property
    def group(self):
        """
        Gets the group of this StackScaleRequestV2.
        name of the instance group

        :return: The group of this StackScaleRequestV2.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this StackScaleRequestV2.
        name of the instance group

        :param group: The group of this StackScaleRequestV2.
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")

        self._group = group

    @property
    def desired_count(self):
        """
        Gets the desired_count of this StackScaleRequestV2.
        scaling adjustment of the instance groups

        :return: The desired_count of this StackScaleRequestV2.
        :rtype: int
        """
        return self._desired_count

    @desired_count.setter
    def desired_count(self, desired_count):
        """
        Sets the desired_count of this StackScaleRequestV2.
        scaling adjustment of the instance groups

        :param desired_count: The desired_count of this StackScaleRequestV2.
        :type: int
        """
        if desired_count is None:
            raise ValueError("Invalid value for `desired_count`, must not be `None`")

        self._desired_count = desired_count

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
        if not isinstance(other, StackScaleRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
