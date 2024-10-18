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

from flowly.core.enumerations import AttributeFlags
from flowly.core.base_entity import BaseEntity
if TYPE_CHECKING:
    from flowly.core.node import Node
    from flowly.core.edge import Edge


class Attribute(BaseEntity):
    """
    Represents an attribute within a node-based system.

    An `Attribute` instance is associated with a parent node and represents a specific
    data port within that node. Attributes can serve as inputs, outputs, or options,
    depending on the role specified by the `flag`. The attribute's data can be of any type,
    defined by the `data_type` attribute. An attribute can be connected to other attributes
    through edges and may be linked to multiple edges if `is_multi_edge` is set to `True`.
    """

    __slots__ = ('_name', '_data', '_data_type', '_flag', '_parent', '_edges', '_is_multi_edge')

    def __init__(
        self,
        uuid: Optional[UUID] = None,
        name: str = "Attribute",
        data: Any = None,
        data_type: type = Any,
        flag: AttributeFlags = AttributeFlags.INPUT,
        parent: Optional[Node] = None,
        is_multi_edge: bool = True,
        edges: Optional[list[Edge]] = None
    ) -> None:
        """
        Initializes an `Attribute` instance.

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
        :param is_multi_edge: Determines if the attribute can connect to multiple edges. Defaults to True.
        :type is_multi_edge: bool
        :param edges: A list of edges connected to this attribute. Defaults to an empty list.
        :type edges: Optional[list[Edge]]
        """
        super().__init__(uuid=uuid)
        self._name: str = name
        self._data: Any = data
        self._data_type: type = data_type
        self._flag: AttributeFlags = flag
        self._parent: Optional[Node] = parent
        self._is_multi_edge: bool = is_multi_edge
        self._edges: list[Edge] = edges or []

    def __repr__(self) -> str:
        """
       Returns a string representation of the attribute for debugging purposes.

       :return: A string representation of the attribute.
       :rtype: str
       """
        return f"<{type(self).__module__}.{type(self).__name__} {self._name} (UUID: {self.uuid}) at {hex(id(self))}>"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Attribute:
        """
        Creates an `Attribute` instance from a dictionary.

        :param data: A dictionary containing the attribute properties.
        :type data: dict[str, Any]
        :return: An instance of `Attribute`.
        :rtype: Attribute
        :raises ValueError: If required fields are missing or invalid.
        """
        required_keys: list[str] = ['uuid', 'name', 'data', 'data_type', 'flag', 'is_multi_edge']
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
        is_multi_edge: bool = data.get('is_multi_edge', True)

        # Assume that the application will resolve the edge instances based on UUIDs
        edges: list[Edge] = []  # This should be populated later in the actual context

        return cls(
            uuid=uuid, name=name, data=data_value, data_type=data_type, flag=flag, parent=parent,
            is_multi_edge=is_multi_edge, edges=edges
        )

    @classmethod
    def from_json(cls, json_str: str) -> Attribute:
        """
        Creates an `Attribute` instance from a JSON string.

        :param json_str: A JSON string representing the attribute.
        :type json_str: str
        :return: An instance of `Attribute`.
        :rtype: Attribute
        """
        data: dict[str, Any] = json.loads(json_str)
        return cls.from_dict(data)

    @property
    def name(self) -> str:
        """
        Gets or sets the name of the attribute.

        :return: The name of the attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def data(self) -> Any:
        """
        Gets or sets the data associated with the attribute.

        :return: The data associated with the attribute.
        :rtype: Any
        """
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @property
    def data_type(self) -> type:
        """
        Gets the data type of the attribute.

        :return: The type of the data.
        :rtype: type
        """
        return self._data_type

    @property
    def flag(self) -> AttributeFlags:
        """
        Gets the flag indicating the role of the attribute.

        :return: The flag for this attribute.
        :rtype: AttributeFlags
        """
        return self._flag

    @property
    def parent(self) -> Optional[Node]:
        """
        Gets or sets the parent node associated with the attribute.

        :return: The parent node of the attribute, if any.
        :rtype: Optional[Node]
        """
        return self._parent

    @parent.setter
    def parent(self, value: Optional[Node]) -> None:
        self._parent = value

    @property
    def is_multi_edge(self) -> bool:
        """
        Gets whether the attribute allows multiple edges to be connected.

        :return: True if multiple edges are allowed, otherwise False.
        :rtype: bool
        """
        return self._is_multi_edge

    @property
    def edges(self) -> list[Edge]:
        """
        Gets the list of edges connected to the attribute.

        :return: A list of edges.
        :rtype: list[Edge]
        """
        return self._edges

    def connect_edge(self, edge: Edge) -> None:
        """
        Connects an edge to the attribute.

        :param edge: The edge to be connected.
        :type edge: Edge
        :raises ValueError: If `_is_multi_edge` is False and an edge is already connected.
        """
        if not self._is_multi_edge and len(self._edges) >= 1:
            raise ValueError("This attribute does not allow multiple edges.")
        self._edges.append(edge)

    def has_edge(self) -> bool:
        """
        Checks if the attribute is connected to any edges.

        :return: True if there is at least one edge connected, otherwise False.
        :rtype: bool
        """
        return len(self._edges) > 0

    def disconnect_edge(self, edge: Edge) -> None:
        """
        Disconnects an edge from the attribute.

        :param edge: The edge to be disconnected.
        :type edge: Edge
        """
        self._edges.remove(edge)

    def to_dict(self) -> dict[str, Any]:
        """
        Converts the attribute to a dictionary representation.

        :return: A dictionary containing the attribute's properties.
        :rtype: dict[str, Any]
        """
        base_dict = super().to_dict()  # Get the dictionary from BaseEntity
        attribute_dict = {
            'name': self._name,
            'data': self._data,
            'data_type': self._data_type.__name__ if self._data_type else None,
            'flag': self._flag.name,
            'parent': str(self._parent.uuid) if self._parent else None,
            'is_multi_edge': self._is_multi_edge,
            'edges': [str(edge.uuid) for edge in self._edges],  # Store edge UUIDs
        }
        return {**base_dict, **attribute_dict}  # Merge dictionaries

    def to_json(self) -> str:
        """
        Converts the attribute to a JSON string.

        :return: A JSON representation of the attribute.
        :rtype: str
        """
        return json.dumps(self.to_dict())
