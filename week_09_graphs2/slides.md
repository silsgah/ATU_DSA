---
marp: true
theme: default
paginate: true
---

# Week 9: Graphs II (Advanced)
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Algorithms for Weighted Graphs
2. Dijkstra's Algorithm
3. Directed Acyclic Graphs (DAGs)
4. Topological Sorting

---

# 1. The Shortest Path Problem
- Standard BFS works perfectly to find the fastest route if all roads take exactly 1 minute.
- Standard BFS completely fails if you are using Google Maps with highways and slow side-streets.
- We need an algorithm that explores based on accumulated time/distance, not hop count.

---

# 2. Dijkstra's Algorithm 
- Uses a **Min-Heap (Priority Queue)** instead of a standard FIFO queue.
- At every step, it pops off the known location with the absolute shortest accumulated distance from the start point.
- Because of the Min-Heap, the *first* time we hit our target destination, we are mathematically guaranteed it's the fastest route.

---

# 3. Topological Sort (DAGs)
- What if a graph represents university course prerequisites? (Must take 101 before 201).
- We can sort this dependency tree into a linear list using Kahn's Algorithm.
- If we can't complete the sort, the Graph has a cycle (e.g. 101 requires 201 and 201 requires 101), indicating a deadlock!

---

# 4. Disjoint Set Union (DSU) & Amortized Complexity
The Disjoint Set Union (DSU) data structure keeps track of elements partitioned into disjoint subsets.
- **Union by Rank**: Keep trees shallow by attaching the smaller rank tree to the larger one.
- **Path Compression**: Connect nodes directly to the root during `find()` calls.
- **Complexity**: Combining both techniques yields an amortized time complexity of $O(\alpha(N))$ per operation, where $\alpha(N)$ is the extremely slow-growing **Inverse Ackermann function** ($\alpha(N) < 5$ for all practical inputs).

---

# 5. Shortest Paths with Negative Weights
Dijkstra's algorithm assumes non-negative edge weights and can fail if negative edges are present:
- **Dijkstra's Failure**: Once a node is popped from the Min-Heap, Dijkstra assumes its shortest path is final. A negative edge found later can violate this.
- **Bellman-Ford Algorithm**: Relaxes all edges $V-1$ times. Correctly handles negative weights and detects negative cycles in $O(V \cdot E)$ time.
- **Floyd-Warshall Algorithm**: Computes all-pairs shortest paths in $O(V^3)$ time using Dynamic Programming ($O(V^2)$ space by updating in-place).
