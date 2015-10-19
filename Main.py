from Turing import Turing
from Node import Node
from Edge import Edge
import string

__author__ = 'ervin_main'
input_file_name = 'in.txt'
output_file_name = 'out.txt'

# main entrance of the project

if __name__ == "__main__":

    try:
        file = open(input_file_name, "r")
        nodes = []
        turing_machine = Turing()

        while True:
            line = file.readline().rstrip()

            if not line:
                break

            if line == 'NODES':
                line = file.readline().rstrip()

                while True:
                    if not line or line == '/NODES':
                        break
                    else:
                        node_str = line.split(' ', 1)
                        node_name = node_str[0]
                        if len(node_str) > 1:
                            node_name, node_prop = node_str
                            if node_prop == 'S':
                                node = Node(node_name, True, False)
                            elif node_prop == 'E':
                                node = Node(node_name, False, True)
                            elif node_prop == 'ES' or node_prop == 'SE':
                                node = Node(node_name, True, True)
                        else:
                            node = Node(node_name)
                        turing_machine.add_node(node)
                        line = file.readline().rstrip()

            elif line == 'EDGES':

                line = file.readline().rstrip()

                while True:
                    if not line or line == '/EDGES':
                        break
                    else:
                        first_node, second_node, source, destination, direction = line.rstrip().split(' ', 4)
                        node1 = turing_machine.get_node(first_node)
                        node2 = turing_machine.get_node(second_node)
                        edge = Edge(node2, source, destination, direction)
                        node1.add_edge(edge)
                        line = file.readline().rstrip()

        file.close()
        # turing_machine.print_machine()
        word = [0, 0, 1, 0, 1, 1]
        turing_machine.generateWord(word)
    except IOError:
        print("File could not be opened!")

