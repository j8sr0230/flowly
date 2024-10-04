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

import logging

import networkx as nx
import matplotlib.pyplot as plt

from node_graph import NodeGraph
from node_item import NodeItem
from custom_exceptions import AttributeDateTypeException


if __name__ == "__main__":
    print("Welcome to flowly 0.0.1")

    node_graph: NodeGraph = NodeGraph()

    node_1: NodeItem = NodeItem(name="Node Item 1")
    node_2: NodeItem = NodeItem(name="Node Item 2")
    node_3: NodeItem = NodeItem(name="Node Item 3")

    node_graph.add_node_item(node=node_1)
    node_graph.add_node_item(node=node_2)
    node_graph.add_node_item(node=node_3)

    try:
        node_graph.add_edge_item(out_node_item=node_1, out_attribute_id=0, in_node_item=node_2, in_attribute_id=0)
        node_graph.add_edge_item(out_node_item=node_1, out_attribute_id=0, in_node_item=node_2, in_attribute_id=1)
    except AttributeDateTypeException as attr_ex:
        logging.warning("No edge created! " + attr_ex.message)

    print([n.name for n in node_graph.neighbors(node_1.output_attributes[0])])

    node_pos: dict = nx.spring_layout(node_graph, seed=1)
    nx.draw(node_graph, pos=node_pos)
    nx.draw_networkx_labels(node_graph, pos=node_pos)
    plt.show()
