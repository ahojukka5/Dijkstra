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


def test_destination_only_node_is_listed_and_counted():
    graph = Graph()
    graph.add_edge('source', 'leaf', 1)
    assert set(graph.get_nodes()) == {'source', 'leaf'}
    assert graph.get_number_of_nodes() == 2
    assert graph.get_adjacent_nodes('leaf') == set()
    assert 'Node leaf: connected to 0 nodes' in str(graph)


def test_leaf_nodes_in_cyclic_graph():
    graph = Graph()
    for source, target in [
        ('external', 'stopper'), ('goal', 'step2'), ('goal', 'stopper'),
        ('step1', 'start'), ('step1', 'step2'), ('step2', 'goal'),
        ('stopper', 'external'), ('stopper', 'goal'), ('stopper', 'step1'),
    ]:
        graph.add_edge(source, target, 1)
    assert set(graph.get_nodes()) == {
        'stopper', 'step1', 'step2', 'goal', 'start', 'external',
    }
    assert graph.get_number_of_nodes() == 6


def test_constructor_includes_leaf_nodes_without_changing_input():
    adjacency = {'source': {'leaf'}, 'isolated': set()}
    graph = Graph(adjacency, {('source', 'leaf'): 2})
    assert set(graph.get_nodes()) == {'source', 'leaf', 'isolated'}
    assert graph.get_number_of_nodes() == 3
    assert graph.get_adjacent_nodes('leaf') == set()
    assert set(adjacency) == {'source', 'isolated'}


def test_repeated_edges_self_loops_and_leaf_becoming_source():
    graph = Graph()
    graph.add_edge('source', 'leaf', 1)
    graph.add_edge('source', 'leaf', 2)
    graph.add_edge('leaf', 'leaf', 3)
    graph.add_edge('leaf', 'next', 4)
    assert set(graph.get_nodes()) == {'source', 'leaf', 'next'}
    assert graph.get_number_of_nodes() == 3
    assert graph.get_adjacent_nodes('leaf') == {'leaf', 'next'}
    assert graph.get_edge_weight('source', 'leaf') == 2


def test_empty_graph_has_no_nodes():
    graph = Graph()
    assert list(graph.get_nodes()) == []
    assert graph.get_number_of_nodes() == 0
