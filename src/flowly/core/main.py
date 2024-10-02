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

import networkx as nx
import matplotlib.pyplot as plt

from node import Node


if __name__ == "__main__":
    print("Welcome to flowly 0.0.1")

    G: nx.DiGraph = nx.DiGraph()

    node_1: Node = Node(name="Node 1")
    node_2: Node = Node(name="Node 2")
    node_3: Node = Node(name="Node 3")

    G.add_edge(node_1, node_2)
    G.add_edge(node_1, node_3)
    G.add_edge(node_2, node_3)
    print([n.name for n in G.neighbors(node_2)])

    node_pos: dict = nx.spring_layout(G)
    nx.draw(G, pos=node_pos)
    nx.draw_networkx_labels(G, pos=node_pos)
    plt.show()
