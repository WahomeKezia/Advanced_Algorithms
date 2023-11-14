## Question2

****
Graph to work on

![image](https://github.com/WahomeKezia/Advanced_Algorithms/blob/main/Graphs/Q2-Graph.png)

**1. Required descriptions**
---
- How many nodes n? 6
- How many edges m? 4
- How many adjacent edges e? [(a,b),(b,d), (d,e) (a,c) (f,)]

**2.Tasks to be completed**
---
Complete the bfs function, If a node is unreachable, its distance is -1.

bfs has the following parameter(s):

int n: the number of nodes
int m: the number of edges
int e[]: start and end nodes for edges
int s: the node to start traversals from
Consider the weight (w) of every edge to be 4.

Returns
int d[ ]: the distances to nodes in increasing distance number order, ensure the negative values at the end of the array

The file: https://github.com/WahomeKezia/Advanced_Algorithms/blob/main/Graphs/Q2_BFS.py 

Returns: [-1, -1, 0, 4, 4, 8, 12]
