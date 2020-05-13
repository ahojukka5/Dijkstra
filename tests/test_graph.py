from dijkstra import Graph


def test_graph():
    G = Graph()
    G.add_edge(1, 2, 3)
    G.add_edge(1, 3, 2)
    assert G.get_edge_weight(1, 2) == 3
    assert G.get_edge_weight(1, 3) == 2
    assert G.get_adjacent_nodes(1) == [2, 3]
