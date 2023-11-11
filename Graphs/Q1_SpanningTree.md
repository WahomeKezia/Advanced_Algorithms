##Question one 
---
For the graph below use Kruskal's algorithm and Prim's algorithm to find a minimum weight spanning
tree. Your answer should include a complete list of the edges, indicating which edges you take for \
your tree in the course of running the algorithm.

![image](https://github.com/WahomeKezia/Advanced_Algorithms/assets/90443938/937deea9-a25d-4514-b0cd-5783a610f1a9)


Tasks to be done

1. Use Kruskal's algorithm and write a program that will return the minimum spanning tree of the graph given (the graph contains all edges of the parent graph).
2. Draw the graph from the resulting values returned from task 1.

3. Use prim's algorithm and write a program that will return the minimum spanning tree of the graph given (the graph contains all edges of the parent graph)
4. Draw the graph and from the resulting values returned from task 3

5. Justify whether or not the two graphs are the same.
6. Justify which algorithm is better and why?

##Solution 
---
**Spanning Tree:**
A spanning tree of a connected, undirected graph is a subgraph that is a tree and connects all the vertices together. A minimum weight spanning tree is a spanning tree with the minimum possible total edge weight. 

For the graph in the image above , 

G= (V,E) (v= vertices ,  E=edges)

**Vertices **

In this graph |v| = 12
V = `{a,f,k,j,h,e,i,c,g,h,d,b}` 
This vertices can be represented as = { 0-a 1=b 2=c 3=d 4=e 5=f 6=g 7=h 8=i 9=j 10=k 11=l } 

**Edges**
For the edges , 
|E| = 22
`{ af =5 ,  ac =8   , al=14 ,cg=12 , ci=10, cl=8, if=8 , ie=16 , eh=8 , el=15 ,hj=16, hl=15, hb=12 , jk=5 jg=5, kf=16 ,kb=47, fd=94, fb=20, dg=22 ,gl=13 db=8  } `

This can represented as the source vertex, destination vertex, and the weight of the edgeas below

{(0, 5, 5) ,(0, 2, 8) ,(0, 11, 14),(2, 6, 12),(2, 8, 10) ,(2, 11, 8) ,(8, 5, 8)
(8, 4, 16) ,(7, 4, 8) ,(4, 11, 15) ,(7, 9, 16) ,(11, 7, 15) ,(7, 2, 12) ,(9, 10, 5)
(9, 6, 5), (10, 5, 16) ,(10, 1, 47) ,(3, 5, 94) ,(1, 5, 20), (3, 6, 22) ,(6, 11, 13) ,(3, 1, 8) }

With the vertices and edges defined , I applied the** Kruskal** and **Prim's** greedy algorithms to get the minimun Spanning tree:
See the implementation in SpanningTree.py <https://github.com/WahomeKezia/Advanced_Algorithms/blob/main/Graphs/SpanningTree.py>

##Results 
---

1. **Kruskal's Algorithm**:
Minimum Spanning Tree: [[0, 5, 5], [9, 10, 5], [9, 6, 5], [0, 2, 8], [2, 11, 8], [8, 5, 8], [7, 4, 8], [3, 1, 8], [2, 6, 12], [7, 2, 12], [1, 5, 20]]
  
Total Cost: 99

MST Graph 
![image](https://github.com/WahomeKezia/Advanced_Algorithms/blob/main/Graphs/Kruskal'sMST.jpg)

2. **Prim's Algorithm**:
Minimum Spanning Tree: [[0, 0, 0], [0, 5, 5], [0, 2, 8], [2, 11, 8], [5, 8, 8], [2, 6, 12], [6, 9, 5], [9, 10, 5], [2, 7, 12], [7, 4, 8], [5, 1, 20], [1, 3, 8]]

Total Cost: 99

MST Graph
![image](https://github.com/WahomeKezia/Advanced_Algorithms/blob/main/Graphs/Prim'sMST.jpg)

##Are the Algorithms the same , which is better?
---
The Algorithms return the same cost for mst 
Here are some reasons why Kruskal's and Prim's algorithms may and in this case return the same MST:

**Uniqueness of MST:**
The graph has unique edge weights, there is only one MST, and both algorithms will find and return the same tree.

**Connected Graph:**
The graph is connected, meaning there is a path between every pair of vertices, Kruskal's and Prim's algorithms will build the MST starting from different edges but ultimately converge to the same tree.

- Both algorithms have the same time complexity of O(E log V) in the worst case, where V is the number of vertices and E is the number of edges.
  
**Differences Between the algorithms:**

This is acontrast of the two algorithms that will show which is better when solve a different senario graph
1. Kruskal's algorithm relies on sorting the edges based on their weights, which can have a time complexity of O(E log E), where E is the number of edges while Prim's algorithm is based on selecting vertices and growing the minimum spanning tree from an initial vertex.The time complexity is typically expressed as O(E log V)
2. Kruskal's algorithm is often preferred for sparse graphs (where the number of edges is much less than the square of the number of vertices).Prim's algorithm can be more efficient for dense graphs (where the number of edges is close to the square of the number of vertices).

3. Kruskal's algorithm can handle disconnected graphs, as it processes each edge independently.Prim's algorithm assumes that the graph is connected. If the graph is not connected, you may need to run the algorithm for each connected component.

  


