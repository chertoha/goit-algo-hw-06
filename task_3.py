from data import stations, edges
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

G = nx.DiGraph()
G.add_nodes_from(stations)
G.add_edges_from(edges)

shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))

table_data = []
for source, targets in shortest_paths.items():
    for target, path in targets.items():
        table_data.append([source, target, " -> ".join(path)])

headers = ["Source", "Target", "Shortest Path"]
print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, k=0.5, iterations=500)
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Transport Network Graph", fontsize=14)
plt.show()
