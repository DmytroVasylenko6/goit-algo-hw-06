from collections import deque

from task_1 import topo_graph


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


if __name__ == "__main__":
    print("Result from DFS algorithm")
    dfs(topo_graph, "h")
    print("\n")
    print("Result from BFS algorithm")
    bfs(topo_graph, "h")
