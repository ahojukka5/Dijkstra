#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


class Dijkstra(object):

    """ Dijkstra's shortest path algorithm. """

    def __init__(self, G, s):
        self.__dist = dist = dict()
        self.__prev = prev = dict()
        self.__visited = visited = set()
        self.__queue = queue = set()

        self.__dist[s] = 0
        self.__prev[s] = s
        self.__queue.add(s)

        while queue:
            u = min(queue, key=dist.get)
            for v in self.get_adjacent_nodes(G, u):
                if v in visited:
                    continue
                alt = self.get_distance(u) + self.get_edge_weight(G, u, v)
                if alt < self.get_distance(v):
                    dist[v] = alt
                    prev[v] = u
                    queue.add(v)
            queue.remove(u)
            visited.add(u)

    @staticmethod
    def get_adjacent_nodes(G, u):
        return G.get_adjacent_nodes(u)

    @staticmethod
    def get_edge_weight(G, u, v):
        return G.get_edge_weight(u, v)

    def get_distance(self, u):
        return self.__dist.get(u, math.inf)
