import random


class Node:
    def __init__(self, name, neighbours=None):
        neighbours = list()
        self.neighbours = neighbours
        self.name = name

    def set_neighbours(self, new_neighbours):
        '''
            unpacks new_neighbours into tuples, adds it to self.neighbours
        '''
        for neighbour in new_neighbours:
            self.neighbours.append(neighbour)

    def get_trust(self, neighbour):
        '''
            Gets trust for specific neighbours
        '''
        for locate, trust in self.neighbours:
            if locate == neighbour:
                return trust


# list of all nodes
nodes = []

# creates a n amount of nodes with incimented names.


def createNodes(node_amount):
    for i in range(node_amount+1):
        nodes.append(Node("n" + str(i)))

# creates trust value from node1 to node 2


def createTrust(node1, node2, forward_trust, back_trust):
    node1_index = nodes.index(node1)
    node2_index = nodes.index(node2)

    nodes[node1_index].set_neighbours([(nodes[node2_index], forward_trust)])
    nodes[node2_index].set_neighbours([(nodes[node1_index], back_trust)])

# testing random trust values


def randomiseTrusts(node_amount):
    for i in range(node_amount):
        createTrust(nodes[i], nodes[i+1], (random.randint(1,
                    100))/100, (random.randint(1, 100))/100)


# creation definition
createNodes(100)
randomiseTrusts(100)


if __name__ == '__main__':
    print(nodes[0].get_trust(nodes[1]))
    print(nodes[1].get_trust(nodes[0]))
