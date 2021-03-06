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


class SecurityGroupDetails(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'security_group_id': 'str',
        'security_group_ids': 'list[str]',
        'security_rules': 'list[SecurityRuleDetails]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'security_group_id': 'securityGroupId',
        'security_group_ids': 'securityGroupIds',
        'security_rules': 'securityRules'
    }

    def __init__(self, id=None, name=None, description=None, security_group_id=None, security_group_ids=None, security_rules=None):
        """
        SecurityGroupDetails - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._security_group_id = None
        self._security_group_ids = None
        self._security_rules = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if security_group_id is not None:
          self.security_group_id = security_group_id
        if security_group_ids is not None:
          self.security_group_ids = security_group_ids
        if security_rules is not None:
          self.security_rules = security_rules

    @property
    def id(self):
        """
        Gets the id of this SecurityGroupDetails.

        :return: The id of this SecurityGroupDetails.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityGroupDetails.

        :param id: The id of this SecurityGroupDetails.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SecurityGroupDetails.

        :return: The name of this SecurityGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityGroupDetails.

        :param name: The name of this SecurityGroupDetails.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SecurityGroupDetails.

        :return: The description of this SecurityGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityGroupDetails.

        :param description: The description of this SecurityGroupDetails.
        :type: str
        """

        self._description = description

    @property
    def security_group_id(self):
        """
        Gets the security_group_id of this SecurityGroupDetails.

        :return: The security_group_id of this SecurityGroupDetails.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """
        Sets the security_group_id of this SecurityGroupDetails.

        :param security_group_id: The security_group_id of this SecurityGroupDetails.
        :type: str
        """

        self._security_group_id = security_group_id

    @property
    def security_group_ids(self):
        """
        Gets the security_group_ids of this SecurityGroupDetails.

        :return: The security_group_ids of this SecurityGroupDetails.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """
        Sets the security_group_ids of this SecurityGroupDetails.

        :param security_group_ids: The security_group_ids of this SecurityGroupDetails.
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def security_rules(self):
        """
        Gets the security_rules of this SecurityGroupDetails.

        :return: The security_rules of this SecurityGroupDetails.
        :rtype: list[SecurityRuleDetails]
        """
        return self._security_rules

    @security_rules.setter
    def security_rules(self, security_rules):
        """
        Sets the security_rules of this SecurityGroupDetails.

        :param security_rules: The security_rules of this SecurityGroupDetails.
        :type: list[SecurityRuleDetails]
        """

        self._security_rules = security_rules

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
        if not isinstance(other, SecurityGroupDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
