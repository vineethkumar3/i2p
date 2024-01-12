import os
import networkx as nx
import matplotlib.pyplot as plt
import json

def plotGraph(data):
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

def combine_json():
    combined_json={}
    for filename in os.listdir("./results"):
        with open(filename , 'r') as data:
            json_data=json.load(data)
            combined_json.update(json_data)
    print(combined_json)
    plotGraph().draw_graph(json.loads(json.dumps(combined_json,indent=2)))

combine_json()
