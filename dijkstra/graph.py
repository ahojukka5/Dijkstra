class Graph(object):

    """ Directed, acyclis graph with edge weights. """

    def __init__(self):
        self.__adjacency_list = dict()
        self.__edge_weights = dict()

    def add_edge(self, u, v, w):
        """ Add a new edge u -> v to graph with edge weight w. """
        self.__edge_weights[u, v] = w
        if u not in self.__adjacency_list:
            self.__adjacency_list[u] = list()
        self.__adjacency_list[u].append(v)

    def get_edge_weight(self, u, v):
        """ Get edge weight of edge between u and v. """
        return self.__edge_weights[u, v]

    def get_adjacent_nodes(self, u):
        """ Get nodes adjacent to u. """
        return self.__adjacency_list[u]