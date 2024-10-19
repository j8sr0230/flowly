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

from typing import Optional
from uuid import UUID

from flowly.core.base_entity import BaseEntity
from flowly.core.attribute import Attribute


class Node(BaseEntity):
    """
    Represents a node within a node-based system.

    A `Node` is an entity that serves as a container for multiple attributes, which can represent data inputs, outputs,
    or configuration options. Each `Node` has a unique identifier (UUID) and a name, and it can be connected to other
    nodes through its attributes. This class provides mechanisms for managing the node's attributes and their
    connections.

    Inherits:
       BaseEntity: Provides common functionality for entities within the node-based system.
    """

    __slots__ = ('_name', '_attributes')

    def __init__(self, uuid: Optional[UUID] = None, name: str = "Node") -> None:
        """
        Initializes a new instance of the `Node` class.

        :param uuid: The unique identifier for the node. If not provided, a new UUID will be generated.
        :type uuid: Optional[UUID]
        :param name: The name of the node. Defaults to "Node".
        :type name: str
        """
        super().__init__(uuid=uuid)

        self._name: str = name
        self._attributes: list[Attribute] = []

    @property
    def name(self) -> str:
        """
        Gets or sets the name of the node.

        :return: The name of the attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def attributes(self) -> list[Attribute]:
        """
        Gets the list of registered node attributes.

        :return: A list of attributes.
        :rtype: list[Attribute]
        """
        return self._attributes
