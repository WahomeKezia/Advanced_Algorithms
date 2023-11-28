import sys

def tsp(graph, current, visited, memo):
    if tuple(visited) in memo:
        return memo[tuple(visited)]

    if all(visited):
        return graph[current][0]  # Return to the starting location

    min_distance = sys.maxsize

    for i in range(len(graph)):
        if not visited[i] and graph[current][i] != 0:
            visited[i] = True
            distance = graph[current][i] + tsp(graph, i, visited, memo)
            min_distance = min(min_distance, distance)
            visited[i] = False

    memo[tuple(visited)] = min_distance
    return min_distance

def shortest_path(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True  # Starting from the first location
    memo = {}
    return tsp(graph, 0, visited, memo)

#Graph 
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Test the program
shortest_distance = shortest_path(graph)
print(f"The shortest distance is: {shortest_distance}")
