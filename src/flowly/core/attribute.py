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
from typing import TYPE_CHECKING, Any, Optional
from uuid import UUID
import json

from flowly.core.base_entity import BaseEntity
from flowly.core.enumerations import AttributeFlags
if TYPE_CHECKING:
    from flowly.core.node import Node


class Attribute(BaseEntity):
    """
    Represents an attribute within a node-based system.

    Each `Attribute` instance is associated with a parent node and represents a specific
    data point within the node. Attributes can be inputs, outputs, or options depending on
    the role defined by the `flag`. The attribute's data can be of any type, and the type
    is specified with the `data_type` attribute.

    Attributes:
        _name (str): The name of the attribute.
        _data (Any): The data associated with the attribute.
        _data_type (type): The type of the data.
        _flag (AttributeFlags): The attribute flag indicating its role (e.g., input, output, option).
        _parent (Optional[Node]): The parent node that this attribute belongs to.
    """

    __slots__ = ('_name', '_data', '_data_type', '_flag', '_parent')

    def __init__(
        self,
        uuid: Optional[UUID] = None,
        name: str = "Attribute",
        data: Any = None,
        data_type: type = Any,
        flag: AttributeFlags = AttributeFlags.INPUT,
        parent: Optional[Node] = None,
    ) -> None:
        """
        Initializes an Attribute instance.

        :param uuid: The unique identifier for the attribute. If not provided, a new UUID will be generated.
        :type uuid: Optional[UUID]
        :param name: The name of the attribute. Defaults to "Attribute".
        :type name: str
        :param data: The data associated with the attribute. Can be any type. Defaults to None.
        :type data: Any
        :param data_type: The type of the data. Defaults to Any.
        :type data_type: type
        :param flag: The attribute flag indicating its role (e.g., input, output, option). Defaults to AttributeFlags.INPUT.
        :type flag: AttributeFlags
        :param parent: The parent node to which this attribute belongs. Defaults to None.
        :type parent: Optional[Node]
        """
        super().__init__(uuid=uuid)
        self._name: str = name
        self._data: Any = data
        self._data_type: type = data_type
        self._flag: AttributeFlags = flag
        self._parent: Optional[Node] = parent

    def __repr__(self) -> str:
        """Returns a string representation of the attribute for debugging."""
        return f"<{type(self).__module__}.{type(self).__name__} {self._name} (UUID: {self.uuid}) at {hex(id(self))}>"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Attribute:
        """
        Creates an Attribute instance from a dictionary, including base properties.

        :param data: A dictionary containing the attribute properties.
        :type data: Dict[str, Any]
        :return: An instance of `Attribute`.
        :rtype: Attribute
        :raises ValueError: If required fields are missing or invalid.
        """
        # Check for required keys and their types
        required_keys: list[str] = ['uuid', 'name', 'data', 'data_type', 'flag']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: '{key}' in input data.")

        try:
            uuid: UUID = UUID(data['uuid'])  # Validate UUID
        except ValueError as e:
            raise ValueError(f"Invalid UUID: {data['uuid']}") from e

        name: str = data['name']
        data_value: Any = data['data']

        data_type_str: str = data['data_type']
        try:
            data_type: type = eval(data_type_str) # Validate data_type
        except NameError:
            raise ValueError(f"Invalid data type: {data_type_str}")

        try:
            flag: AttributeFlags = AttributeFlags[data['flag']]  # Validate flag
        except KeyError:
            raise ValueError(f"Invalid flag value: {data['flag']}")

        parent: Optional[Node] = None  # The parent must be resolved in the actual application context

        # Create an Attribute instance using the extracted values
        return cls(uuid=uuid, name=name, data=data_value, data_type=data_type, flag=flag, parent=parent)

    @classmethod
    def from_json(cls, json_str: str) -> Attribute:
        """
        Creates an Attribute instance from a JSON string.

        :param json_str: A JSON string representing the attribute.
        :type json_str: str
        :return: An instance of `Attribute`.
        :rtype: Attribute
        """
        data: dict[str, Any] = json.loads(json_str)
        return cls.from_dict(data)

    @property
    def name(self) -> str:
        """Returns the name of the attribute."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets the name of the attribute."""
        self._name = value

    @property
    def data(self) -> Any:
        """Returns the data associated with the attribute."""
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        """Sets the data associated with the attribute."""
        self._data = value

    @property
    def data_type(self) -> type:
        """Returns the data type of the attribute."""
        return self._data_type

    @property
    def flag(self) -> AttributeFlags:
        """Returns the flag indicating the role of the attribute."""
        return self._flag

    @property
    def parent(self) -> Optional[Node]:
        """Returns the parent node of the attribute, if any."""
        return self._parent

    @parent.setter
    def parent(self, value: Optional[Node]) -> None:
        """Sets the parent associated with the attribute."""
        self._parent = value

    def to_dict(self) -> dict[str, Any]:
        """
        Converts the attribute to a dictionary representation, including base properties.

        :return: A dictionary with all the attribute's properties.
        :rtype: Dict[str, Any]
        """
        base_dict = super().to_dict()  # Get the dictionary from BaseEntity
        attribute_dict = {
            'name': self._name,
            'data': self._data,
            'data_type': self._data_type.__name__ if self._data_type else None,
            'flag': self._flag.name,
            'parent': str(self._parent.uuid) if self._parent else None,
        }
        return {**base_dict, **attribute_dict}  # Merge dictionaries

    def to_json(self) -> str:
        """
        Converts the attribute to a JSON string.

        :return: A JSON string representing the attribute.
        :rtype: str
        """
        return json.dumps(self.to_dict())
