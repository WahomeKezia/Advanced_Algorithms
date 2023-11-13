from collections import defaultdict, deque

def bfs(n, m, edges, start):
    graph = defaultdict(list)
    distances = [-1] * (n + 1)

    # Construct the graph
    for edge in edges:
        if len(edge) == 2:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)  # assuming the graph is undirected
        elif len(edge) == 1:
            # Handle single-value tuple, assuming it represents a single node
            u = edge[0]
            graph[u] = []

    # Perform BFS
    queue = deque([start])
    distances[start] = 0

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 4  # assuming edge weight is 4
                queue.append(neighbor)

    # Sort the distances in increasing order
    distances.sort()

    return distances

if __name__ == "__main__":
    n = 6  # number of nodes
    m = 4  # number of edges
    edges = [(1, 2), (2, 4), (4, 5), (1, 3), (6,)]  # list of edges
    start = 1  # starting node

    result = bfs(n, m, edges, start)

    # Print the result
    print(result)
