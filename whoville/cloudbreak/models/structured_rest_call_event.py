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


class StructuredRestCallEvent(object):
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
        'type': 'str',
        'operation': 'OperationDetails',
        'rest_call': 'RestCallDetails',
        'duration': 'int',
        'status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'operation': 'operation',
        'rest_call': 'restCall',
        'duration': 'duration',
        'status': 'status'
    }

    def __init__(self, type=None, operation=None, rest_call=None, duration=None, status=None):
        """
        StructuredRestCallEvent - a model defined in Swagger
        """

        self._type = None
        self._operation = None
        self._rest_call = None
        self._duration = None
        self._status = None

        if type is not None:
          self.type = type
        if operation is not None:
          self.operation = operation
        if rest_call is not None:
          self.rest_call = rest_call
        if duration is not None:
          self.duration = duration
        if status is not None:
          self.status = status

    @property
    def type(self):
        """
        Gets the type of this StructuredRestCallEvent.

        :return: The type of this StructuredRestCallEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StructuredRestCallEvent.

        :param type: The type of this StructuredRestCallEvent.
        :type: str
        """

        self._type = type

    @property
    def operation(self):
        """
        Gets the operation of this StructuredRestCallEvent.

        :return: The operation of this StructuredRestCallEvent.
        :rtype: OperationDetails
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this StructuredRestCallEvent.

        :param operation: The operation of this StructuredRestCallEvent.
        :type: OperationDetails
        """

        self._operation = operation

    @property
    def rest_call(self):
        """
        Gets the rest_call of this StructuredRestCallEvent.

        :return: The rest_call of this StructuredRestCallEvent.
        :rtype: RestCallDetails
        """
        return self._rest_call

    @rest_call.setter
    def rest_call(self, rest_call):
        """
        Sets the rest_call of this StructuredRestCallEvent.

        :param rest_call: The rest_call of this StructuredRestCallEvent.
        :type: RestCallDetails
        """

        self._rest_call = rest_call

    @property
    def duration(self):
        """
        Gets the duration of this StructuredRestCallEvent.

        :return: The duration of this StructuredRestCallEvent.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this StructuredRestCallEvent.

        :param duration: The duration of this StructuredRestCallEvent.
        :type: int
        """

        self._duration = duration

    @property
    def status(self):
        """
        Gets the status of this StructuredRestCallEvent.

        :return: The status of this StructuredRestCallEvent.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StructuredRestCallEvent.

        :param status: The status of this StructuredRestCallEvent.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, StructuredRestCallEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other