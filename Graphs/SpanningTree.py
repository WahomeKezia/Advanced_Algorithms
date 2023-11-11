import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(graph):
    result = []
    total_cost = 0 #Initialize the total cost
    graph.graph.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = [i for i in range(graph.vertices)]
    rank = [0] * graph.vertices

    for edge in graph.graph:
        u, v, w = edge
        root_u = find_parent(parent, u)
        root_v = find_parent(parent, v)

        if root_u != root_v:
            result.append(edge)
            total_cost += w  # Add the weight to the total cost
            union(parent, rank, root_u, root_v)

    return result , total_cost

def prim(graph):
    result = []
    total_costp = 0  # Initialize the total cost
    visited = [False] * graph.vertices
    heap = [(0, 0, 0)]  # (weight, source, destination)

    while heap:
        w, u, v = heapq.heappop(heap)

        if not visited[v]:
            result.append([u, v, w])
            total_costp += w  # Add the weight to the total cost
            visited[v] = True

            for edge in graph.graph:
                if edge[0] == v and not visited[edge[1]]:
                    heapq.heappush(heap, (edge[2], edge[0], edge[1]))
                elif edge[1] == v and not visited[edge[0]]:
                    heapq.heappush(heap, (edge[2], edge[1], edge[0]))

    return result , total_costp

# Example usage with your provided graph:
g = Graph(12)
g.add_edge(0, 5, 5)
g.add_edge(0, 2, 8)
g.add_edge(0, 11, 14)
g.add_edge(2, 6, 12)
g.add_edge(2, 8, 10) 
g.add_edge(2, 11, 8)
g.add_edge(8, 5, 8)
g.add_edge(8, 4, 16)
g.add_edge(7, 4, 8)
g.add_edge(4, 11, 15)
g.add_edge(7, 9, 16)
g.add_edge(11, 7, 15)
g.add_edge(7, 2, 12)
g.add_edge(9, 10, 5)
g.add_edge(9, 6, 5)
g.add_edge(10, 5, 16)
g.add_edge(10, 1, 47)
g.add_edge(3, 5, 94)
g.add_edge(1, 5, 20)
g.add_edge(3, 6, 22)
g.add_edge(6, 11, 13)
g.add_edge(3, 1, 8)

print("Kruskal's Algorithm:")
edges, total_cost = kruskal(g)
print("Minimum Spanning Tree:", edges)
print("Total Cost:", total_cost)

print("\nPrim's Algorithm:")
edges, total_costp = prim(g)
print("Minimum Spanning Tree:", edges)
print("Total Cost:", total_costp)

