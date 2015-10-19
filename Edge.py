__author__ = 'ervin_main'


class Edge:
    def __init__(self, to_node, old_symbol, new_symbol, direction):
        self.__to_node = to_node
        self.__old_symbol = old_symbol
        self.__new_symbol = new_symbol
        self.__direction = direction

    def get_to_node(self):
        return self.__to_node

    def get_old_symbol(self):
        return self.__old_symbol

    def get_new_symbol(self):
        return self.__new_symbol

    def get_direction(self):
        return self.__direction

    def get_direction_value(self):
        value = 0
        if self.__direction == "L":
            value = 1
        else:
            if self.__direction == "R":
                value = -1
        return value




