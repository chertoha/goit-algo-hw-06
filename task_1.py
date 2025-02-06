import networkx as nx
import matplotlib.pyplot as plt
from data import stations, edges

G = nx.DiGraph()

G.add_nodes_from(stations)
G.add_edges_from(edges)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, k=0.5, iterations=500)
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes (stations): {num_nodes}")
print(f"Number of edges (routes): {num_edges}\n")

print("Node degrees:")
degrees_list = list(G.degree)
for node, degree in degrees_list:
    print(f"{node}: {degree}")

print("\nIn-degree and Out-degree for nodes:")
for node in G.nodes:
    in_degree = G.in_degree[node]
    out_degree = G.out_degree[node]
    print(f"{node}: In-degree = {in_degree}, Out-degree = {out_degree}")

print("\nNode centrality (betweenness):")
centrality = nx.betweenness_centrality(G)
for node, value in centrality.items():
    print(f"{node}: {value:.2f}")

print("\nConclusions:")
print("1. Central Station має найвищу центральність, оскільки вона з'єднує багато районів.")
print("2. Airport, University, Harbor та Industrial Zone, а також нові вузли Intermediary 1 та Intermediary 2 діють як важливі сполучні вузли.")
print("3. Граф є орієнтованим, що моделює напрямки транспортних маршрутів.")


plt.title("Transport Network Graph", fontsize=14)
plt.show()
