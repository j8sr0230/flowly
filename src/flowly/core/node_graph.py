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
import logging

import networkx as nx
from flowly.core.attribute_item import AttributeFlags

if TYPE_CHECKING:
    from flowly.core.base_item import BaseItem
    from flowly.core.attribute_item import AttributeItem
    from flowly.core.node_item import NodeItem


# Configure logging with timestamp and more context
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


class NodeGraph:
    def __init__(self) -> None:
        self._node_items: list[NodeItem] = []
        self._main_graph: nx.DiGraph = nx.DiGraph()

    @property
    def node_items(self) -> list[NodeItem]:
        return self._node_items

    @property
    def main_graph(self) -> nx.DiGraph:
        return self._main_graph

    def add_node_item(self, node_item: NodeItem) -> None:
        """Adds the node_item to the items list and its internal graph to the main graph."""
        self._node_items.append(node_item)
        self._main_graph: nx.DiGraph = nx.compose(self._main_graph, node_item.internal_graph)

    @staticmethod
    def get_attribute_item_by_id(node_item: NodeItem, attribute_id: int) -> Optional[AttributeItem]:
        """Retrieve attribute item by its ID, or return None if not found."""
        if 0 <= attribute_id < len(node_item.attribute_items):
            return node_item.attribute_items[attribute_id]
        return None

    # def add_node_group_item(self, node_items: list[NodeItem]) -> nx.Graph:
    #     attribute_items: list[BaseItem] = []
    #     for node in node_items:
    #         attribute_items.extend(node.attribute_items)
    #
    #     inner_items: list[BaseItem] = attribute_items + node_items
    #     outer_items: list[BaseItem] = [item for item in self.nodes if item not in inner_items]
    #
    #     temp_graph: nx.DiGraph = self.copy()
    #     temp_graph.remove_edges_from(
    #         (item, neighbour, data)
    #         for item, neighbour in self.adj.items()
    #         if item in inner_items
    #         for neighbour, data in neighbour.items()
    #         if neighbour in outer_items
    #     )
    #     temp_graph.remove_edges_from(
    #         (item, neighbour, data)
    #         for item, neighbour in self.adj.items()
    #         if item in outer_items
    #         for neighbour, data in neighbour.items()
    #         if neighbour in inner_items
    #     )
    #
    #     return temp_graph
    #
    #     # sub_graph: nx.Graph = self.subgraph(node_items + inner_items)
    #     # return sub_graph
    #
    def validate_connection(self, out_attribute_item: Optional[AttributeItem],
                            in_attribute_item: Optional[AttributeItem]) -> Optional[str]:
        """
        Validates if a connection between two attribute_items is possible.
        Returns an error message if validation fails, or None if the connection is valid.
        """
        if not out_attribute_item:
            return "Output attribute item does not exist."

        if out_attribute_item.flag is AttributeFlags.INPUT:
            return "Cannot use output attribute item as input."

        if not in_attribute_item:
            return "Input attribute item does not exist."

        if in_attribute_item.flag is AttributeFlags.OUTPUT:
            return "Cannot use input attribute item as output."

        if out_attribute_item.parent is in_attribute_item.parent:
            return "Cannot connect attribute_items from the same node item."

        if out_attribute_item.flag is in_attribute_item.flag:
            return "Cannot connect inputs to inputs or outputs to outputs."

        if (out_attribute_item.data_type != in_attribute_item.data_type and
                not (out_attribute_item.data_type == Any or in_attribute_item.data_type == Any)):
            return "Cannot connect attribute items with incompatible data types."

        if nx.has_path(self._main_graph, in_attribute_item, out_attribute_item):
            return "Cyclic dependency found."

        return None

    def can_connect(self, out_attribute_item: AttributeItem, in_attribute_item: AttributeItem) -> bool:
        """
        Determines if two attribute_items can be connected, performs validation, checks for cycles, and logs any issues.
        Returns True if the connection is valid, False otherwise.
        """
        message: Optional[str] = self.validate_connection(out_attribute_item, in_attribute_item)
        if message:
            logging.warning(message)
            return False
        return True

    def add_edge_item(self, out_node_item: NodeItem, out_attribute_id: int,
                      in_node_item: NodeItem, in_attribute_id: int) -> None:
        """Attempts to add an edge between two node attribute_items."""
        out_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(out_node_item, out_attribute_id)
        in_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(in_node_item, in_attribute_id)

        if self.can_connect(out_attr_item, in_attr_item):
            self._main_graph.add_edge(out_attr_item, in_attr_item)
