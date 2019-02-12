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


class HardwareInfoGroupResponse(object):
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
        'recovery_mode': 'str',
        'name': 'str',
        'hardware_infos': 'list[HardwareInfoResponse]'
    }

    attribute_map = {
        'recovery_mode': 'recoveryMode',
        'name': 'name',
        'hardware_infos': 'hardwareInfos'
    }

    def __init__(self, recovery_mode=None, name=None, hardware_infos=None):
        """
        HardwareInfoGroupResponse - a model defined in Swagger
        """

        self._recovery_mode = None
        self._name = None
        self._hardware_infos = None

        if recovery_mode is not None:
          self.recovery_mode = recovery_mode
        if name is not None:
          self.name = name
        if hardware_infos is not None:
          self.hardware_infos = hardware_infos

    @property
    def recovery_mode(self):
        """
        Gets the recovery_mode of this HardwareInfoGroupResponse.
        recovery mode of the hostgroup's nodes

        :return: The recovery_mode of this HardwareInfoGroupResponse.
        :rtype: str
        """
        return self._recovery_mode

    @recovery_mode.setter
    def recovery_mode(self, recovery_mode):
        """
        Sets the recovery_mode of this HardwareInfoGroupResponse.
        recovery mode of the hostgroup's nodes

        :param recovery_mode: The recovery_mode of this HardwareInfoGroupResponse.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTO"]
        if recovery_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `recovery_mode` ({0}), must be one of {1}"
                .format(recovery_mode, allowed_values)
            )

        self._recovery_mode = recovery_mode

    @property
    def name(self):
        """
        Gets the name of this HardwareInfoGroupResponse.

        :return: The name of this HardwareInfoGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HardwareInfoGroupResponse.

        :param name: The name of this HardwareInfoGroupResponse.
        :type: str
        """

        self._name = name

    @property
    def hardware_infos(self):
        """
        Gets the hardware_infos of this HardwareInfoGroupResponse.
        Metadata of instances.

        :return: The hardware_infos of this HardwareInfoGroupResponse.
        :rtype: list[HardwareInfoResponse]
        """
        return self._hardware_infos

    @hardware_infos.setter
    def hardware_infos(self, hardware_infos):
        """
        Sets the hardware_infos of this HardwareInfoGroupResponse.
        Metadata of instances.

        :param hardware_infos: The hardware_infos of this HardwareInfoGroupResponse.
        :type: list[HardwareInfoResponse]
        """

        self._hardware_infos = hardware_infos

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
        if not isinstance(other, HardwareInfoGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
