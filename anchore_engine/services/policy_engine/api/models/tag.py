# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class Tag(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id=None, registry_name=None, repository=None, name=None):  # noqa: E501
        """Tag - a model defined in Swagger

        :param user_id: The user_id of this Tag.  # noqa: E501
        :type user_id: str
        :param registry_name: The registry_name of this Tag.  # noqa: E501
        :type registry_name: str
        :param repository: The repository of this Tag.  # noqa: E501
        :type repository: str
        :param name: The name of this Tag.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'user_id': str,
            'registry_name': str,
            'repository': str,
            'name': str
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'registry_name': 'registry_name',
            'repository': 'repository',
            'name': 'name'
        }

        self._user_id = user_id
        self._registry_name = registry_name
        self._repository = repository
        self._name = name

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.  # noqa: E501
        :rtype: Tag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self):
        """Gets the user_id of this Tag.

        The catalog user id that scopes this tag value. NOT a username on the source registry  # noqa: E501

        :return: The user_id of this Tag.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Tag.

        The catalog user id that scopes this tag value. NOT a username on the source registry  # noqa: E501

        :param user_id: The user_id of this Tag.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def registry_name(self):
        """Gets the registry_name of this Tag.

        The registry record name in the catalog to identify the repository. Scoped by the user_id. Eg. dockerhub  # noqa: E501

        :return: The registry_name of this Tag.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        """Sets the registry_name of this Tag.

        The registry record name in the catalog to identify the repository. Scoped by the user_id. Eg. dockerhub  # noqa: E501

        :param registry_name: The registry_name of this Tag.
        :type registry_name: str
        """

        self._registry_name = registry_name

    @property
    def repository(self):
        """Gets the repository of this Tag.

        Repository name, including any source registry user namespace for the tag. e.g. library/centos or bitnami/node  # noqa: E501

        :return: The repository of this Tag.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Tag.

        Repository name, including any source registry user namespace for the tag. e.g. library/centos or bitnami/node  # noqa: E501

        :param repository: The repository of this Tag.
        :type repository: str
        """

        self._repository = repository

    @property
    def name(self):
        """Gets the name of this Tag.

        The name of the tag. e.g. latest, 8.0, or 5.4-alpine  # noqa: E501

        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        The name of the tag. e.g. latest, 8.0, or 5.4-alpine  # noqa: E501

        :param name: The name of this Tag.
        :type name: str
        """

        self._name = name