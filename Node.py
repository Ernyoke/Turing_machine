import copy

__author__ = 'ervin_main'


class Node:

    def __init__(self, name='', is_start_point=False, is_endpoint=False):
        self.__name = copy.deepcopy(name)
        self.__is_start_point = is_start_point
        self.__is_endpoint = is_endpoint
        self.__edges = []

    def add_edge(self, edge):
        self.__edges.append(edge)

    def get_name(self):
        return self.__name

    def is_start_point(self):
        return self.__is_star_tpoint

    def is_endpoint(self):
        return self.__is_endpoint

    def get_name(self):
        return self.__name

    def get_path(self, symbol):
        symbol = str(symbol)
        for edge in self.__edges:
            if edge.get_old_symbol() == symbol:
                return edge
        return None

    def print_edges(self):
        for edge in self.__edges:
            print(''.join([self.__name, ' ', edge.get_to_node().get_name(), ' ',
                           edge.get_old_symbol(),  ' ', edge.get_new_symbol(),
                           ' ', edge.get_direction()]))






