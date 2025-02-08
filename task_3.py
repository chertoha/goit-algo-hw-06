from data import stations, graph
from tabulate import tabulate


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    visited = []

    while len(visited) < len(graph):
        min_distance = float('inf')
        current_node = None

        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        visited.append(current_node)

        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes


def get_shortest_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path


shortest_paths = {}
for station in stations:
    distances, previous_nodes = dijkstra(graph, station)
    for target in stations:
        if station != target:
            path = get_shortest_path(previous_nodes, station, target)
            shortest_paths[(station, target)] = path


table_data = []
for (source, target), path in shortest_paths.items():
    table_data.append([source, target, " -> ".join(path)])

headers = ["Source", "Target", "Shortest Path"]
print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
