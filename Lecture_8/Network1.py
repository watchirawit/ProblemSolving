import matplotlib.pyplot as plt
import networkx as nx

G = nx.dodecahedral_graph()
nx.draw(G)
plt.show()