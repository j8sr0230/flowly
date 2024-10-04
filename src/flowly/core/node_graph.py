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

if TYPE_CHECKING:
    from attribute_item import AttributeItem
    from node_item import NodeItem


class NodeGraph(nx.DiGraph):
    def __init(self) -> None:
        super().__init__()

    @staticmethod
    def get_attribute_item_by_id(node_item: NodeItem, attribute_id) -> Optional[AttributeItem]:
        """Retrieve attribute item by its ID, or return None if not found."""
        if 0 <= attribute_id < len(node_item.attributes):
            return node_item.attributes[attribute_id]
        return None

    @staticmethod
    def log_and_return(message: str, node_item: NodeItem, attribute_id: int) -> None:
        """Logs a warning and returns None."""
        logging.warning(f"{message} Node: {node_item.name}, Attribute ID: {attribute_id}")
        return None

    def add_node_item(self, node: NodeItem) -> None:
        """Adds a node to the graph, linking its input and output attributes internally."""
        for attribute in node.attributes:
            if attribute.is_input:
                # noinspection PyTypeChecker
                self.add_edge(attribute, node, type="internal")
            else:
                # noinspection PyTypeChecker
                self.add_edge(node, attribute, type="internal")

    def add_edge_item(self, out_node_item: NodeItem, out_attribute_id: int,
                      in_node_item: NodeItem, in_attribute_id: int) -> None:
        """Attempts to add an edge between two node attributes and checks for cycles."""

        # Get the attributes by ID
        out_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(
            node_item=out_node_item, attribute_id=out_attribute_id
        )
        in_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(
            node_item=in_node_item, attribute_id=in_attribute_id
        )

        # Edge validation: check if attributes exist
        if not out_attr_item:
            return self.log_and_return("Output attribute item does not exist.", out_node_item, out_attribute_id)

        if not in_attr_item:
            return self.log_and_return("Input attribute item does not exist.", in_node_item, in_attribute_id)

        # Prevent connection between attributes of the same node
        if out_attr_item.parent is in_attr_item.parent:
            return self.log_and_return("Cannot connect attributes from the same node item.",
                                       in_node_item, in_attribute_id)

        # Prevent connecting two inputs or two outputs
        if out_attr_item.is_input == in_attr_item.is_input:
            return self.log_and_return("Cannot connect inputs to inputs or outputs to outputs.",
                                       in_node_item, in_attribute_id)

        # Check for incompatible data types
        if (out_attr_item.data_type != in_attr_item.data_type and
                not Any in [out_attr_item.data_type, in_attr_item.data_type]):
            return self.log_and_return("Cannot connect attribute items with incompatible data types.",
                                       in_node_item, in_attribute_id)

        # Add the edge and check for cycles
        self.add_edge(out_attr_item, in_attr_item, type="external")

        try:
            # Detect cycle and handle it by removing the edge
            cycle_edges: list[tuple] = nx.find_cycle(self)
            if cycle_edges:
                self.remove_edge(out_attr_item, in_attr_item)
                return self.log_and_return("Cyclic dependency found.", in_node_item, in_attribute_id)

        except nx.NetworkXNoCycle:
            pass  # No cycle detected, everything is fine
