import random
import time


class Node:
    ''' 
        This class will be used to create node objects
    '''

    def __init__(self, trust, age=None, nationality=None, political=None, sexuality=None, sex=None):
        self.trust = trust

        # 13 is the minimum is for social media (legally)
        age = random.randint(13, 80)
        # each number representing different nationalities
        nationality = random.randint(1, 5)
        # each corner of the polical compass and the middle
        political = random.randint(1, 5)
        # to keep it simple: 4 sexualities
        sexuality = random.randint(1, 4)
        # to keep it simple: 3 sexes
        sex = random.randint(1, 3)

        self.age = age
        self.nationality = nationality
        self.political = political
        self.sexuality = sexuality
        self.sex = sex

    def setTrust(self, trust):
        self.trust = trust


# creating a list of node objects
# 1000 objs: 0.005s
# 1000000 objs: 4.617s

nodes = list()
for i in range(1000):
    nodes.append(Node(0))


def attributes_to_trustvalue(node1, node2):
    # trust value between 2 nodes
    pass
