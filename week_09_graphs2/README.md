# Week 09: Graphs II (Advanced)

## 1. Weighted Graphs and Shortest Paths
In Week 8, we used Breadth-First Search (BFS) to find the shortest path. This only works reliably for **Unweighted Graphs** (where every edge costs exactly 1 unit to traverse). 

What if a graph is **Weighted**? For instance, Google Maps calculating the fastest route between cities where highways take 10 minutes and side streets take 45. Standard BFS would completely fail because it counts "number of roads" instead of "number of minutes".

For this, we use **Dijkstra's Algorithm**.

### Dijkstra's Algorithm
Dijkstra's is essentially a Breadth-First Search that uses a **Min-Heap (Priority Queue)** instead of a standard FIFO Queue.
Instead of exploring "the node 1 hop away, then 2 hops away," it explores "the node with the shortest accumulated weight from the start point".

*Time Complexity:* $O((V+E) \log V)$ where $V$ is vertices and $E$ is edges.

## 2. Directed Acyclic Graphs (DAGs) and Topo Sort
What happens when a graph is Directed (arrows) and Acyclic (no loops)? This usually represents a **Dependency Graph** (e.g., University course prerequisites: Must take 101 before 201).

**Topological Sorting** provides a linear ordering of vertices such that for every directed edge $u \rightarrow v$, vertex $u$ comes before $v$ in the ordering. 

We can solve this efficiently using **Kahn's Algorithm** (which tracks In-Degrees using a Queue) or via a Depth First Search stack append.

## Practical Assignment (`practice.py`)
1. Implement Dijkstra's Algorithm to find the shortest routing distance.
2. Implement Kahn's Algorithm to solve the "Course Schedule" problem.
