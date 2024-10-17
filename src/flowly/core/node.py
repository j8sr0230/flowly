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

from typing import Optional, Any
from uuid import UUID

import networkx as nx

from flowly.core.hashable import Hashable
from flowly.core.attribute import Attribute, AttributeFlags
from flowly.core.operator_item import OperatorItem


class Node(Hashable):
    def __init__(self, name: str = "Node Item", uuid: Optional[UUID] = None) -> None:
        super().__init__(name=name, uuid=uuid)

        self._attribute_items: list[Attribute] = [
            Attribute(name="A", data=0, data_type=int, flag=AttributeFlags.INPUT, parent=self),
            Attribute(name="B", data=0, data_type=int, flag=AttributeFlags.INPUT, parent=self),
            Attribute(name="Res", data=None, data_type=Any, flag=AttributeFlags.OUTPUT, parent=self)
        ]

        self._operator_item: OperatorItem = OperatorItem(name="Add", parent=self)

        self._internal_graph: nx.DiGraph = nx.DiGraph()
        self.update_internal_graph()

    @property
    def attribute_items(self) -> list[Attribute]:
        return self._attribute_items

    @property
    def operator_item(self) -> OperatorItem:
        return self._operator_item

    @property
    def internal_graph(self) -> nx.DiGraph:
        return self._internal_graph

    def update_internal_graph(self) -> None:
        self._internal_graph.clear()

        for attribute in self.attribute_items:
            if attribute.flag is AttributeFlags.INPUT:
                # noinspection PyTypeChecker
                self._internal_graph.add_edge(attribute, self._operator_item)
            else:
                # noinspection PyTypeChecker
                self._internal_graph.add_edge(self._operator_item, attribute)

