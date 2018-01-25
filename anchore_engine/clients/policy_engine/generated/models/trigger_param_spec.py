# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TriggerParamSpec(object):
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
        'name': 'str',
        'description': 'str',
        'required': 'bool',
        'validator': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'required': 'required',
        'validator': 'validator'
    }

    def __init__(self, name=None, description=None, required=None, validator=None):
        """
        TriggerParamSpec - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._required = None
        self._validator = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if required is not None:
          self.required = required
        if validator is not None:
          self.validator = validator

    @property
    def name(self):
        """
        Gets the name of this TriggerParamSpec.
        Parameter name as it appears in policy document

        :return: The name of this TriggerParamSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TriggerParamSpec.
        Parameter name as it appears in policy document

        :param name: The name of this TriggerParamSpec.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TriggerParamSpec.

        :return: The description of this TriggerParamSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TriggerParamSpec.

        :param description: The description of this TriggerParamSpec.
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """
        Gets the required of this TriggerParamSpec.
        Is this a required parameter or optional

        :return: The required of this TriggerParamSpec.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this TriggerParamSpec.
        Is this a required parameter or optional

        :param required: The required of this TriggerParamSpec.
        :type: bool
        """

        self._required = required

    @property
    def validator(self):
        """
        Gets the validator of this TriggerParamSpec.
        If present, a definition for validation of input. Typically a jsonschema object that can be used to validate an input against.

        :return: The validator of this TriggerParamSpec.
        :rtype: object
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """
        Sets the validator of this TriggerParamSpec.
        If present, a definition for validation of input. Typically a jsonschema object that can be used to validate an input against.

        :param validator: The validator of this TriggerParamSpec.
        :type: object
        """

        self._validator = validator

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
        if not isinstance(other, TriggerParamSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other