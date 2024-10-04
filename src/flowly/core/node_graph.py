#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2024 Ronny Scharf-W. <ronny.scharf08@gmail.com>         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

from __future__ import annotations
from typing import TYPE_CHECKING

import networkx as nx

if TYPE_CHECKING:
    from attribute_item import AttributeItem
    from node_item import NodeItem


class NodeGraph(nx.DiGraph):
    def __init(self) -> None:
        pass

    def add_node_item(self, node: NodeItem) -> None:
        for attribute in node.attributes:
            if attribute.is_input:
                # noinspection PyTypeChecker
                self.add_edge(attribute, node, type="internal")
            else:
                # noinspection PyTypeChecker
                self.add_edge(node, attribute, type="internal")


    def add_edge_item(self, start_attribute: AttributeItem, end_attribute: AttributeItem) -> None:
        self.add_edge(start_attribute, end_attribute, type="external")
