import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()


G.add_edges_from([('A','B'),('A','M'),('A','L'),('B','C'),('B','D'),
                  ('B','N'),('B','O'),('C','D'),('D','E'),('D','O'),
                  ('E','F'),('F','G'),('F','N'),('G','H'),('H','N'),
                  ('H','I'),('H','P'),('P','O'),('P','I'),('P','M'),
                  ('I','J'),('J','K'),('K','M'),('K','L')])



print('A neighbors')
Alist = nx.all_neighbors(G,'A')
Ao = []
Ao1 = []
for k in Alist:
    print(k)
    mlist = nx.all_neighbors(G,k)
    for m in mlist:
        if m != 'A':
            Ao.append(m)
            Ao1.append(m)
    print('neighbors',k,'is',Ao1)
    Ao1 = []
Ao = set(Ao)
print('All neighbors :',Ao)   
        

print('E neighbors')
Elist = nx.all_neighbors(G,'E')
Eo = []
Eo1 = []
for k in Elist:
    print(k)
    clist = nx.all_neighbors(G,k)
    for c in clist:
        if c != 'E':
            Eo.append(c)
            Eo1.append(c)
    print('neighbors',k,'is',Eo1)
    Eo1 = []
Eo = set(Eo)
print('All neighbors :',Eo)

print('I neighbors')
Ilist = nx.all_neighbors(G,'I')
Io = []
Io1 = []
for k in Ilist:
    print(k)
    jlist = nx.all_neighbors(G,k)
    for j in jlist:
        if j != 'I':
            Io.append(j)
            Io1.append(j)
    print('neighbors',k,'is',Io1)
    Io1 = []
Io = set(Io)
all_cet = Ao & Eo & Io
print('All neighbors :',Io)

print('The Centroid is:',list(all_cet))


