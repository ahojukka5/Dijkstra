#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from dijkstra import Graph, DijkstraSPF
from dijkstra.dijkstra import AbstractDijkstraSPF


def test_dijkstra():
    nodes = ("S", "T", "A", "B", "C", "D", "E", "F", "G")
    S, T, A, B, C, D, E, F, G = nodes

    graph = Graph()
    graph.add_edge(S, A, 4)
    graph.add_edge(S, A, 4)
    graph.add_edge(S, B, 3)
    graph.add_edge(S, D, 7)
    graph.add_edge(A, C, 1)
    graph.add_edge(B, S, 3)
    graph.add_edge(B, D, 4)
    graph.add_edge(C, E, 1)
    graph.add_edge(C, D, 3)
    graph.add_edge(D, E, 1)
    graph.add_edge(D, T, 3)
    graph.add_edge(D, F, 5)
    graph.add_edge(E, G, 2)
    graph.add_edge(G, E, 2)
    graph.add_edge(G, T, 3)
    graph.add_edge(T, F, 5)

    dijkstra = DijkstraSPF(graph, S)

    for v in nodes:
        print("%3s %3s" % (v, dijkstra.get_distance(v)))

    assert dijkstra.get_distance(T) == 10
    assert dijkstra.get_path(T) == ["S", "D", "T"]


def test_abstract_dijkstra_spf():
    graph = Graph()

    with pytest.raises(NotImplementedError):
        AbstractDijkstraSPF.get_adjacent_nodes(graph, 0)

    with pytest.raises(NotImplementedError):
        AbstractDijkstraSPF.get_edge_weight(graph, 0, 1)
