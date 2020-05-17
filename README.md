# Dijkstra

[![Python CI][ci-badge]][ci-url]
[![Coverate Status][coveralls-img]][coveralls-url]

![](docs/example1.gif)

Package author: Jukka Aho (@ahojukka5, ahojukka5@gmail.com)

Package implements Dijkstra's shortest path finding algorithm.

## Installing package

To install the most recent package from Python Package Index (PyPi), use git:

```bash
pip install dijkstra
```

To install the development version, you can install the package directly from
the GitHub:

```bash
pip install git+git://github.com/ahojukka5/dijkstra.git
```

[ci-badge]: https://github.com/ahojukka5/gmshparser/workflows/Python%20CI/badge.svg
[ci-url]: https://github.com/ahojukka5/dijkstra/actions
[coveralls-img]: https://coveralls.io/repos/github/ahojukka5/dijkstra/badge.svg?branch=master
[coveralls-url]: https://coveralls.io/github/ahojukka5/dijkstra?branch=master

# Usage

Package implements two classes, `DijkstraSPF` and `Graph`. The above example can
be solved with the following code:

```python
S, T, A, B, C, D, E, F, G = list("STABCDEFG")

graph = Graph()
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
```

It's not mandatory to use `Graph`. To use your own data structure for graph, you
need to subclass `AbstractDijkstraSPF` and implement two functions connecting
graph object to the shortest path finder algorithms: `get_adjacent_nodes` and
`get_edge_weight`. For example, implementation using `Graph` is the following:

```python
class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        return G.get_adjacent_nodes(u)

    @staticmethod
    def get_edge_weight(G, u, v):
        return G.get_edge_weight(u, v)
```
