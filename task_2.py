import networkx as nx
import matplotlib.pyplot as plt
from data import stations, edges

G = nx.DiGraph()
G.add_nodes_from(stations)
G.add_edges_from(edges)


def dfs_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path

    neighbors = list(graph.neighbors(start))
    if "South District" in neighbors:
        neighbors.remove("South District")
        neighbors.insert(0, "South District")
    for neighbor in neighbors:
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, end, path + [neighbor])


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == end:
            yield path

        neighbors = list(graph.neighbors(vertex))
        if "North District" in neighbors:
            neighbors.remove("North District")
            neighbors.insert(0, "North District")
        for neighbor in neighbors:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))


start_node = "Central Station"
end_node = "Airport"

print(f"Шляхи DFS від {start_node} до {end_node}:")
dfs_paths_result = list(dfs_paths(G, start_node, end_node))
for path in dfs_paths_result:
    print(path)

print(f"\nШляхи BFS від {start_node} до {end_node}:")
bfs_paths_result = list(bfs_paths(G, start_node, end_node))
for path in bfs_paths_result:
    print(path)

print("\nПорівняння:")
print("DFS досліджує шляхи вглиб, перш ніж досліджувати сусідів, тому може спочатку знаходити довші шляхи.")
print("BFS досліджує всіх сусідів на поточному рівні, перш ніж переходити на наступний рівень, що гарантує знаходження найкоротшого шляху.")

if dfs_paths_result == bfs_paths_result:
    print("DFS та BFS знайшли однаковий шлях.")
else:
    print("DFS та BFS знайшли різні шляхи через їхні різні стратегії пошуку.")
    print("DFS зазвичай знаходить шлях: ", dfs_paths_result[0])
    print("BFS завжди знаходить найкоротший шлях: ", bfs_paths_result[0])


def draw_path(path, color):
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                           edge_color=color, width=4, arrowsize=20)


pos = nx.spring_layout(G)
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

for path in dfs_paths_result:
    draw_path(path, 'red')

for path in bfs_paths_result:
    draw_path(path, 'green')

plt.title("Шляхи DFS (червоний) та BFS (зелений)", fontsize=14)
plt.show()
