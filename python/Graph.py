import json

import networkx as nx
import matplotlib.pyplot as plt
import helper_functions
class Graph:

    def draw_graph(self,data):

        G = nx.DiGraph()
        for key1, value1 in data.items():
            for key, value in value1.items():
                for id in range(len(value)-1):
                    G.add_edge(value[id],value[id+1])

        mapping = {node: str(node)[:4] for node in G.nodes()}
        G_relabel = nx.relabel_nodes(G, mapping)
        nx.draw_networkx(G_relabel, with_labels=True)
        #nx.draw_circular(G_relabel, with_labels=True)
        plt.show()

        nx.draw_

if __name__=='__main__':
    obj=Graph()
    with open('data.json','r') as data:
        output=json.load(data)

    obj.draw_graph(output)
