import matplotlib.pyplot as plt
import networkx as nx
Province_start = input('Province Start: ')
Province_end = input('Province End: ')

G = nx.Graph()

G.add_edge('Chiang Rai',"Phayao",weight=92)
G.add_edge("Chiang Rai",'Lampang',weight=229)
G.add_edge('Chiang Rai',"Chiang Mai",weight=190)
G.add_edge('Phayao',"Nan",weight=148)
G.add_edge('Phayao',"Phrae",weight=143)
G.add_edge('Phayao',"Lampang",weight=142)
G.add_edge("Chiang Mai",'Mae Hong Son ',weight=237)
G.add_edge('Chiang Mai',"Lampang",weight=114)
G.add_edge('Chiang Mai',"Lamphun ",weight=39)
G.add_edge('Lampang',"Lamphun ",weight=82)
G.add_edge('Lampang',"Tak",weight=188)
G.add_edge('Lampang',"Sukhothai",weight=195)
G.add_edge('Lampang',"Phrae",weight=96)
G.add_edge('Tak',"Mae Hong Son ",weight=508)
G.add_edge('Tak',"Lamphun ",weight=241)
G.add_edge('Tak',"Sukhothai",weight=85)
G.add_edge('Tak',"Kamphaeng Phe",weight=62)
G.add_edge('Phrae',"Nan",weight=119)
G.add_edge('Phrae',"Uttaradit",weight=72)
G.add_edge('Phrae',"Sukhothai",weight=163)
G.add_edge('Sukhothai',"Uttaradit",weight=91)
G.add_edge('Sukhothai',"Kamphaeng Phe",weight=71)
G.add_edge('Sukhothai',"Phitsanulok",weight=58)
G.add_edge('Phitsanulok',"Uttaradit",weight=108)
G.add_edge('Phitsanulok',"Kamphaeng Phe",weight=110)
G.add_edge('Phitsanulok',"Phichit",weight=57)
G.add_edge('Phitsanulok',"Phetchabun",weight=177)
G.add_edge('Nakhon Sawan',"Uthai Thani",weight=43)
G.add_edge('Nakhon Sawan',"Kamphaeng Phe",weight=132)
G.add_edge('Nakhon Sawan',"Phichit",weight=104)
G.add_edge('Nakhon Sawan',"Phetchabun",weight=174)
G.add_edge('Phichit',"Phetchabun",weight=133)
G.add_edge('Phichit',"Kamphaeng Phe",weight=100)

print('Province to pass through is:' , 
    nx.shortest_path(G,source=Province_start,target=Province_end,weight='weight'))
print('Distance from',Province_start,'to',Province_end,'is:' , 
    nx.shortest_path_length(G,source=Province_start,target=Province_end,weight='weight'),'Km')



edge_labels = nx.get_edge_attributes(G,'weight')


pos = nx.spring_layout(G)
nx.draw(G,pos ,with_labels=True,font_color="black",font_size="5",node_size= 2000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()