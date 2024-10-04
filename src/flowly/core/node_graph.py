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
from typing import TYPE_CHECKING, Any

import networkx as nx

from custom_exceptions import AttributeIndexException, AttributeDateTypeException

if TYPE_CHECKING:
    from attribute_item import AttributeItem
    from node_item import NodeItem


class NodeGraph(nx.DiGraph):
    def __init(self) -> None:
        super().__init__()

    @staticmethod
    def get_attribute_item_by_id(node_item: NodeItem, attribute_id: int, is_input: bool) -> AttributeItem:
        attributes: list[AttributeItem] = node_item.input_attributes if is_input else node_item.output_attributes
        if 0 <= attribute_id < len(attributes):
            return attributes[attribute_id]

        raise AttributeIndexException(node_item=node_item, attribute_id=attribute_id, is_input=is_input)

    def add_node_item(self, node: NodeItem) -> None:
        for attribute in node.attributes:
            if attribute.is_input:
                # noinspection PyTypeChecker
                self.add_edge(attribute, node, type="internal")
            else:
                # noinspection PyTypeChecker
                self.add_edge(node, attribute, type="internal")

    def add_edge_item(self, out_node_item: NodeItem, out_attribute_id: int,
                      in_node_item: NodeItem, in_attribute_id: int) -> None:
        out_attribute_item: AttributeItem = self.get_attribute_item_by_id(
            node_item=out_node_item, attribute_id=out_attribute_id, is_input=False
        )
        in_attribute_item: AttributeItem = self.get_attribute_item_by_id(
            node_item=in_node_item, attribute_id=in_attribute_id, is_input=True
        )

        if (Any in [out_attribute_item.data_type, in_attribute_item.data_type] or
                out_attribute_item.data_type == in_attribute_item.data_type
        ):
            self.add_edge(out_attribute_item, in_attribute_item, type="external")
        else:
            raise AttributeDateTypeException(
                out_attribute_item=out_attribute_item, in_attribute_item=in_attribute_item
            )
