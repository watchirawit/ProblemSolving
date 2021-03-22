import matplotlib.pyplot as plt
import networkx as nx

G = nx.dodecahedral_graph()

nx.draw(G, with_labels=True,font_color="yellow",node_size= 1000)
plt.show()