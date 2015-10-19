from Node import Node

__author__ = 'ervin_main'


class Turing:
    __nodes = []

    def add_node(self, node):
        self.__nodes.append(node)

    def get_node(self, name):
        for i in self.__nodes:
            if i.get_name() == name:
                return i
        return None

    def get_node_by_nr(self, nr):
        return self.__nodes[nr]

    def print_machine(self):
        for node in self.__nodes:
            node.print_edges()

    def __word_return_first(self, word):
        if len(word) == 0:
            return 'B'
        return word[0]

    def __word_return_last(self, word):
        if len(word) == 0:
            return 'B'
        return word[len(word) - 1]

    def __word_append_symbol(self, word, symbol):
        length = len(word)
        if length == 0 and symbol == 'B':
            pass
        elif length > 0 and word[length - 1] == 'B' and symbol == 'B':
            pass
        else:
            word.append(symbol)

    def __word_prepend_symbol(self, word, symbol):
        length = len(word)
        if length == 0 and symbol == 'B':
            pass
        elif length > 0 and word[0] == 'B' and symbol == 'B':
            pass
        else:
            word.insert(0, symbol)

    def __word_delete_last(self, word):
        if len(word) > 0:
            del word[len(word) - 1]

    def __word_delete_first(self, word):
        if len(word) > 0:
            del word[0]

    def generateWord(self, word):
        right = word
        left = []
        current_node = self.get_node('q0')
        while True:
            if len(right) == 0 and len(left) == 0 and current_node.is_endpoint():
                print("recognized")
                break
            edge = current_node.get_path(self.__word_return_first(right))
            if edge:
                direction = edge.get_direction()
                if direction == 'R':
                    self.__word_append_symbol(left, edge.get_new_symbol())
                    self.__word_delete_first(right)
                    print(''.join([current_node.get_name(), ' -> ', edge.get_to_node().get_name(), ' left:',
                                   ''.join(str(left)), ' right:', ''.join(str(right))]))
                    current_node = edge.get_to_node()
                elif direction == 'L':
                    if edge:
                        self.__word_prepend_symbol(right, edge.get_new_symbol())
                        self.__word_delete_last(left)
                        print(''.join([current_node.get_name(), ' -> ', edge.get_to_node().get_name(), ' left:',
                                   ''.join(str(left)), ' right:', ''.join(str(right))]))
                        current_node = edge.get_to_node()
                    else:
                        # check if it is recognized or not
                        if current_node.is_endpoint():
                            print("recognized!")
                        else:
                            print("not recognized")
                        # break from the loop
                        break
            else:
                print("not recognized")
                break











