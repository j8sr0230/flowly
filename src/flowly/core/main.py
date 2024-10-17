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

# from __future__ import annotations
# from typing import TYPE_CHECKING

# import networkx as nx
# import matplotlib.pyplot as plt
#
# from flowly.core.operator_item import OperatorItem
# from node_graph import NodeGraph
# from node import Node
# if TYPE_CHECKING:
#     from hashable import Hashable

from flowly.core.hashable import Hashable


# Main
if __name__ == "__main__":

    item: Hashable = Hashable()
    print(item)

    json = item.to_json()
    print(json)

    h = Hashable.from_json(json)
    print(h)

    print(h==Hashable())

    # print("Welcome to flowly 0.0.1")
    #
    # node_graph: NodeGraph = NodeGraph()
    #
    # node_1: Node = Node(name="Node Item 1")
    # node_2: Node = Node(name="Node Item 2")
    # node_3: Node = Node(name="Node Item 3")
    #
    # node_graph.add_node_item(node_item=node_1)
    # node_graph.add_node_item(node_item=node_2)
    # node_graph.add_node_item(node_item=node_3)
    #
    # node_graph.add_edge_item(out_node_item=node_1, out_attribute_id=2, in_node_item=node_2, in_attribute_id=0)
    # node_graph.add_edge_item(out_node_item=node_1, out_attribute_id=2, in_node_item=node_2, in_attribute_id=1)
    # node_graph.add_edge_item(out_node_item=node_2, out_attribute_id=2, in_node_item=node_3, in_attribute_id=0)
    # node_graph.add_edge_item(out_node_item=node_3, out_attribute_id=2, in_node_item=node_1, in_attribute_id=0)
    # node_graph.add_edge_item(out_node_item=node_3, out_attribute_id=2, in_node_item=node_1, in_attribute_id=2)
    #
    # neighbor_names = [
    #     f"{n.parent.name}.{n.name}" if hasattr(n, "parent") else f"{n.name}"
    #     for n in node_graph.main_graph.neighbors(node_1.attribute_items[2])
    # ]
    # print(neighbor_names)
    #
    # # Define a custom graph layout
    # node_sizes: list[int] = [600 if type(node) is OperatorItem else 100 for node in node_graph.main_graph]
    # node_labels: dict[Hashable, str] = {
    #     node: f"{node.parent.name}.{node.name}" if hasattr(node, "parent") else node.name for node in node_graph.main_graph
    # }
    # node_pos: dict = nx.spring_layout(node_graph.main_graph, seed=1)
    # nx.draw(node_graph.main_graph, pos=node_pos, with_labels=True, node_size=node_sizes)  # , labels=node_labels,
    # plt.show()

    # sub_graph: nx.Graph = node_graph.add_node_group_item([node_1, node_2])
    # nx.draw(sub_graph, pos=node_pos, with_labels=True)
    # plt.show()

    # print([(n.name, nbrs) for n, nbrs in node_graph.main_graph.adj.items()])
