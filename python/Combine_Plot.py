import os
import networkx as nx
import matplotlib.pyplot as plt
import json

def plotGraph(data):
        G = nx.DiGraph()
        for key1, value1 in data.items():
            for key, value in value1.items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        for id in range(len(value2)-1):
                            G.add_edge(value2[id],value2[id+1])
                else:
                    for id in range(len(value) - 1):
                        G.add_edge(value[id], value[id + 1])

        mapping = {node: str(node)[:4] for node in G.nodes()}
        G_relabel = nx.relabel_nodes(G, mapping)
        #nx.draw_networkx(G_relabel, with_labels=True)
        #nx.draw_networkx(G_relabel, with_labels=True)
        nx.draw_circular(G_relabel, with_labels=True)
        nodes=G.nodes
        #print(nodes)
        vineeth={}
        mydata=[]
        for x in nodes:
         print(dict(G.degree)[x])
         vineeth.update({
             x:dict(G.degree)[x]
         })

         mydata.append(dict(G.degree)[x])
        print(vineeth)
        plt.hist(mydata, bins=max(mydata) - min(mydata) + 1, align='left', rwidth=0.8, edgecolor='black')

         # Add labels and title
        plt.xlabel('Degrees')
        plt.ylabel('Number of Routers')
        plt.title('Router Degrees Histogram')

         # Show the plot
        plt.show()
        #plt.show(G)




def combine_json():
    combined_json={}
    for filename in os.listdir("./results"):
        with open(filename , 'r') as data:
            json_data=json.load(data)
            combined_json.update(json_data)
    with open('data.json', 'w') as file:
        file.write(combined_json)

    #plotGraph().draw_graph(json.loads(json.dumps(combined_json,indent=2)))

if __name__=='__main__':
    combine_json()
    old_char = "'"
    new_char = '"'

    # Read the file, replace the character, and write back the modified data
    with open('data.json', 'r') as file:
        content = file.read()
        modified_content = content.replace(old_char, new_char)

    with open('data.json', 'w') as file:
        file.write(modified_content)
    with open('data.json','r') as data:
        output=json.load(data)
    plotGraph(output,"Combined Graph")


    def exploratory_Tunnels(output):
        exploratory_data={}
        client_data={}
        for key, value in output.items():
            exploratory_data.update({key:{}})
            client_data.update({key:{}})
            for key1, value1 in value.items():
                if key1 == "exploratory_Tunnel":
                    exploratory_data[key]=value1
                elif key1 == "Client_Tunnels":
                    client_data[key]=value1
        return exploratory_data,client_data

    exploratory_data,client_Data=exploratory_Tunnels(output)

    plotGraph(exploratory_data,"Exploratory Tunnels")
    plotGraph(client_Data,"Client Tunnels")
