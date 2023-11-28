import sys

def tsp_memoization(graph, current, visited, memo):
    """
    Recursive function to calculate the shortest path in the Traveling Salesman Problem using memoization.

    Parameters:
    - graph: The adjacency matrix representing the weighted graph.
    - current: The current location (vertex) in the path.
    - visited: A list indicating which vertices have been visited.
    - memo: A memoization dictionary to store previously computed results.

    Returns:
    The shortest distance for the TSP.
    """
    if tuple(visited) in memo:
        return memo[tuple(visited)]

    if all(visited):
        return graph[current][0]  # Return to the starting location

    min_distance = sys.maxsize

    for i in range(len(graph)):
        if not visited[i] and graph[current][i] != 0:
            visited[i] = True
            distance = graph[current][i] + tsp_memoization(graph, i, visited, memo)
            min_distance = min(min_distance, distance)
            visited[i] = False

    memo[tuple(visited)] = min_distance
    return min_distance

def shortest_path_memoization(graph, vertices):
    """
    Function to initiate the Traveling Salesman Problem calculation using memoization.

    Parameters:
    - graph: The adjacency matrix representing the weighted graph.
    - vertices: The list of vertices.

    Returns:
    The shortest distance for the TSP.
    """
    n = len(graph)
    visited = [False] * n
    visited[0] = True  # Starting from the first location
    memo = {}
    return tsp_memoization(graph, 0, visited, memo)

# Specify the vertices and edge weights
vertices = ['A', 'B', 'C', 'D', 'E']
graph = [
    [0, 12, 10, 19, 8],
    [6, 0, 3, 7, 6],
    [15, 7, 0, 2, 20],
    [19, 3, 2, 0, 4],
    [8, 6, 20, 4, 0]
]

# Test the program
shortest_distance = shortest_path_memoization(graph, vertices)
print(f"The shortest distance is: {shortest_distance}")
