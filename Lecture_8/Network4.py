import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()


G.add_edges_from([('A','B'),('A','M'),('A','L'),('B','C'),('B','D'),
                  ('B','N'),('B','O'),('C','D'),('D','E'),('D','O'),
                  ('E','F'),('F','G'),('F','N'),('G','H'),('H','N'),
                  ('H','I'),('H','P'),('P','O'),('P','I'),('P','M'),
                  ('I','J'),('J','K'),('K','M'),('K','L')])

print('Shortest path from E to L is :',
    nx.shortest_path(G,source='E',target='L'))

print('A neighbors')
Alist = nx.all_neighbors(G,'A')
for k in Alist:
    print(k)

print('E neighbors')
Elist = nx.all_neighbors(G,'E')
for k in Elist:
    print(k)

print('I neighbors')
Ilist = nx.all_neighbors(G,'I')
for k in Alist:
    print(k)

print("Shortset path from O to A is : ",
    nx.shortest_path_length(G,source='O',target='A'))


