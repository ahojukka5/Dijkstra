#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from dijkstra import Graph, generate_random_graph


def test_graph():
    G = Graph()
    G.add_edge(1, 2, 3)
    G.add_edge(1, 3, 2)
    assert G.get_edge_weight(1, 2) == 3
    assert G.get_edge_weight(1, 3) == 2
    assert G.get_adjacent_nodes(1) == {2, 3}


def test_random_graph():
    random.seed(1)
    G = generate_random_graph(10, 0.5, 1, 10)
    assert G.get_adjacent_nodes(0) == {1, 2, 6, 7, 9}
    assert G.__str__().startswith("Directed, acyclic graph with 10 nodes")
