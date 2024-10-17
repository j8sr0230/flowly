#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ************************************************************************
# * Copyright (c) 2024 Ronny Scharf-W. <ronny.scharf08@gmail.com>        *
# *                                                                      *
# * This program is free software; you can redistribute it and/or modify *
# * it under the terms of the GNU Lesser General Public License (LGPL)   *
# * as published by the Free Software Foundation; either version 2 of    *
# * the License, or (at your option) any later version.                  *
# * for detail see the LICENSE text file.                                *
# *                                                                      *
# * This program is distributed in the hope that it will be useful,      *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of       *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the         *
# * GNU Library General Public License for more details.                 *
# *                                                                      *
# * You should have received a copy of the GNU Library General Public    *
# * License along with this program; if not, write to the Free Software  *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  *
# * USA                                                                  *
# *                                                                      *
# ************************************************************************

from __future__ import annotations
from uuid import UUID, uuid1
from typing import Any, Optional, Dict
import json


class BaseEntity:
    """
    A base class for objects that can be uniquely identified and compared using a UUID.

    The `BaseEntity` class generates a UUID for each instance, which is used to make instances
    hashable and comparable. If a UUID is not provided during initialization, a new UUID is
    generated automatically. The UUID is immutable after the object is created.

    Features:
        - Provides a unique identifier for each instance using a UUID.
        - Implements hashability and equality comparison based on the UUID.
        - Supports conversion to and from dictionary and JSON representations.
        - Uses `__slots__` to reduce memory usage by limiting instance attributes.

    Examples:
        >>> obj1 = BaseEntity()
        >>> obj2 = BaseEntity()
        >>> obj1 == obj2
        False
        >>> obj1.uuid == obj2.uuid
        False
        >>> obj1_dict = obj1.to_dict()
        >>> obj3 = BaseEntity.from_dict(obj1_dict)
        >>> obj1 == obj3
        True
    """

    __slots__ = ('_uuid', '_hash')  # Use __slots__ to reduce memory usage

    def __init__(self, uuid: Optional[UUID] = None) -> None:
        """
        Initializes a `BaseEntity` instance.

        :param uuid: The UUID for the instance. If not provided, a new UUID is generated
                     using `uuid1()`.
        :type uuid: Optional[UUID]
        """
        self._uuid: UUID = uuid or uuid1()
        self._hash = hash(self._uuid)  # Cache the hash value

    def __eq__(self, other: Any) -> bool:
        """
        Checks if this instance is equal to another `BaseEntity` instance based on the UUID.

        :param other: The other object to compare against.
        :type other: Any
        :return: `True` if the other object is a `BaseEntity` instance with the same UUID, `False` otherwise.
        :rtype: bool
        """
        return isinstance(other, BaseEntity) and self._uuid == other.uuid

    def __hash__(self) -> int:
        """
        Returns the hash value of the instance, based on the cached UUID hash.

        :return: The hash value of the UUID.
        :rtype: int
        """
        return self._hash

    def __repr__(self) -> str:
        """
        Returns a string representation of the instance for debugging.

        :return: A string representation including the module, class name, UUID, and memory address.
        :rtype: str
        """
        return f"<{type(self).__module__}.{type(self).__name__} {self._uuid} at {hex(id(self))}>"

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> BaseEntity:
        """
        Creates an instance from a dictionary.

        :param data: A dictionary containing the UUID.
        :type data: Dict[str, str]
        :return: An instance of `BaseEntity`.
        :rtype: BaseEntity
        """
        if 'uuid' not in data:  # Check for required key
            raise ValueError("Dictionary must contain a 'uuid' key.")

        try:
            uuid: UUID = UUID(data['uuid'])  # Validate UUID
        except ValueError as e:
            raise ValueError(f"Invalid UUID: {data['uuid']}") from e
        return cls(uuid)

    @classmethod
    def from_json(cls, json_str: str) -> BaseEntity:
        """
        Creates an instance from a JSON string.

        :param json_str: A JSON string representing the instance.
        :type json_str: str
        :return: An instance of `BaseEntity`.
        :rtype: BaseEntity
        """
        data: Dict[str, str] = json.loads(json_str)
        return cls.from_dict(data)

    @property
    def uuid(self) -> UUID:
        """
        Returns the UUID of the instance. The UUID is cached after the first access.

        :return: The unique identifier for this instance.
        :rtype: UUID
        """
        return self._uuid

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the instance to a dictionary representation.

        :return: A dictionary with the UUID.
        :rtype: Dict[str, str]
        """
        return {'uuid': str(self._uuid)}


    def to_json(self) -> str:
        """
        Converts the instance to a JSON string.

        :return: A JSON string representing the instance.
        :rtype: str
        """
        return json.dumps(self.to_dict())
