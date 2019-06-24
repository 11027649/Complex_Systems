import networkx as nx

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

from networkx import DiGraph

import pickle

with open("gpickle.pickle", 'rb') as handler:
    G = pickle.load(handler)

text_labels = list(G.nodes)

label_dict = {}
for i, node in enumerate(G.nodes):
    label_dict[node] = text_labels[i]
print(label_dict)
pos = nx.layout.spring_layout(G)


node_sizes = [3 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]

labels = nx.draw_networkx_labels(G, pos, label_dict)
nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='blue')
edges = nx.draw_networkx_edges(G, pos, node_size=node_sizes, arrowstyle='->',
                               arrowsize=10, edge_color=edge_colors,
                               edge_cmap=plt.cm.Blues, width=2)

# set alpha value for each edge
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()
plt.savefig("network.png")
