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


# Configure logging with timestamp and more context
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


class NodeGraph(nx.DiGraph):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_attribute_item_by_id(node_item: NodeItem, attribute_id: int) -> Optional[AttributeItem]:
        """Retrieve attribute item by its ID, or return None if not found."""
        if 0 <= attribute_id < len(node_item.attributes):
            return node_item.attributes[attribute_id]
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

    def validate_connection(self, out_attribute_item: AttributeItem, in_attribute_item: AttributeItem) -> Optional[str]:
        """
        Validates if a connection between two attributes is possible.
        Returns an error message if validation fails, or None if the connection is valid.
        """
        if not out_attribute_item:
            return "Output attribute item does not exist."

        if out_attribute_item.is_input:
            return "Cannot use output attribute item as input."

        if not in_attribute_item:
            return "Input attribute item does not exist."

        if not in_attribute_item.is_input:
            return "Cannot use input attribute item as output."

        if out_attribute_item.parent is in_attribute_item.parent:
            return "Cannot connect attributes from the same node item."

        if out_attribute_item.is_input == in_attribute_item.is_input:
            return "Cannot connect inputs to inputs or outputs to outputs."

        if (out_attribute_item.data_type != in_attribute_item.data_type and
                not (out_attribute_item.data_type == Any or in_attribute_item.data_type == Any)):
            return "Cannot connect attribute items with incompatible data types."

        if nx.has_path(self, in_attribute_item, out_attribute_item):
            return "Cyclic dependency found."

        return None

    def can_connect(self, out_attribute_item: AttributeItem, in_attribute_item: AttributeItem) -> bool:
        """
        Determines if two attributes can be connected, performs validation, checks for cycles, and logs any issues.
        Returns True if the connection is valid, False otherwise.
        """
        message: Optional[str] = self.validate_connection(out_attribute_item, in_attribute_item)
        if message:
            logging.warning(message)
            return False
        return True

    def add_edge_item(self, out_node_item: NodeItem, out_attribute_id: int,
                      in_node_item: NodeItem, in_attribute_id: int) -> None:
        """Attempts to add an edge between two node attributes."""
        out_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(out_node_item, out_attribute_id)
        in_attr_item: Optional[AttributeItem] = self.get_attribute_item_by_id(in_node_item, in_attribute_id)

        if self.can_connect(out_attr_item, in_attr_item):
            self.add_edge(out_attr_item, in_attr_item, type="external")
