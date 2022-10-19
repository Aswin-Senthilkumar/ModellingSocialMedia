import networkx as nx
import matplotlib.pyplot as plt
import random


node_names = [i for i in range(100)]

G = nx.MultiDiGraph()


nodes = []

for i in range(150):
    n1 = random.choice(node_names)
    n2 = random.choice(node_names)

    if n1 is not n2:
        tup = (n1, n2)
        nodes.append(tup)


G.add_edges_from(nodes)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="black")
nx.draw_networkx_labels(G, pos)

plt.show()
