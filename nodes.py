from hashlib import new
from tracemalloc import get_traceback_limit


class Node:
    def __init__(self, neighbours=None):
        neighbours = list()
        self.neighbours = neighbours

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


n1 = Node()
n2 = Node()
n3 = Node()

n1.set_neighbours([(n2, 0.5), (n3, 0.3)])
print(n1.get_trust(n2))
