# Week 09: Graphs II (Advanced) — Lecture & Study Guide

Welcome to Week 09! Today we transition from basic graph traversals (BFS/DFS) to advanced graph algorithms. This guide covers weighted shortest paths, path-finding constraints (negative weights and cycles), all-pairs shortest paths, Disjoint Set Union (DSU), and topological sorting. 

These notes contain the mathematical rigor, proofs, and conceptual models needed to master this week's material and excel on the exam.

---

## Table of Contents
1. [Weighted Graphs & Shortest Paths](#1-weighted-graphs--shortest-paths)
2. [Dijkstra's Algorithm & Negative Weights](#2-dijkstras-algorithm--negative-weights)
3. [The Bellman-Ford Algorithm](#3-the-bellman-ford-algorithm)
4. [The Floyd-Warshall Algorithm (All-Pairs Shortest Paths)](#4-the-floyd-warshall-algorithm-all-pairs-shortest-paths)
5. [Disjoint Set Union (DSU) & Amortized Complexity](#5-disjoint-set-union-dsu--amortized-complexity)
6. [DAGs & Topological Sorting](#6-dags--topological-sorting)

---

## 1. Weighted Graphs & Shortest Paths

In Week 08, we used **Breadth-First Search (BFS)** to find the shortest path in unweighted graphs. BFS is guaranteed to find the shortest path in unweighted graphs because it explores vertices in order of hop-count:
- Visit all nodes at distance 1
- Visit all nodes at distance 2, etc.

However, in real-world systems (like GPS routing), graph edges have **weights** representing costs, times, or distances (e.g., traveling on a highway takes 10 minutes, but a local street takes 45 minutes). 

### Why BFS Fails on Weighted Graphs
Consider the following graph where edges represent travel times:

```text
       [Start: A]
        /      \
    5  /        \ 1
      v          v
    [B] --------> [C]
          2
```
- **BFS Search**: BFS checks paths by edge count. It finds the path $A \rightarrow B$ of length 1 (total cost = 5).
- **Actual Shortest Path**: The path $A \rightarrow C \rightarrow B$ has 2 edges but a total cost of $1 + 2 = 3$. 
- BFS stops when it first hits a node, which means it will incorrectly conclude that the path $A \rightarrow B$ of cost 5 is the shortest.

---

## 2. Dijkstra's Algorithm & Negative Weights

To solve shortest paths on weighted graphs with non-negative edge weights, we use **Dijkstra's Algorithm**.

### The Conceptual Model
Dijkstra's algorithm is structurally identical to BFS, except that we swap the standard FIFO Queue for a **Min-Heap (Priority Queue)**.
- **Queue BFS**: Explores the node with the fewest edges from the start.
- **Priority Queue Dijkstra**: Explores the node with the **smallest accumulated distance** from the start.

### The Algorithm Steps
1. Initialize a `distances` table, setting `distances[start] = 0` and `distances[v] = infinity` for all other vertices $v$.
2. Push `(0, start)` to the Min-Heap.
3. While the Min-Heap is not empty:
   - Pop the element `(dist, u)` with the smallest distance.
   - If `dist > distances[u]`, skip it (we already found a shorter path to `u`).
   - For each neighbor `v` of `u` with edge weight `weight`:
     - Calculate the potential new distance: `new_dist = dist + weight`.
     - If `new_dist < distances[v]`:
       - Update `distances[v] = new_dist`.
       - Push `(new_dist, v)` to the Min-Heap.

### Complexity Analysis
- **Time Complexity**: $O((V + E) \log V)$ using a binary heap representation.
  - Extracting the minimum vertex takes $O(\log V)$, done at most $V$ times: $O(V \log V)$.
  - Decreasing key / pushing to heap takes $O(\log V)$, done at most $E$ times: $O(E \log V)$.
- **Space Complexity**: $O(V)$ to store distances and priority queue elements.

### Why Dijkstra Fails with Negative Edge Weights
Dijkstra's algorithm relies on a **greedy invariant**: *Once a node is popped from the priority queue, its shortest path from the source is finalized and will never be updated.* This invariant is mathematically guaranteed if and only if all edge weights are non-negative ($w \ge 0$).

If negative edge weights are present, this greedy assumption collapses.

#### Counterexample:
```text
       (Start: A)
        /       \
    3  /         \ 4
      v           v
    (B) <------- (C)
           -2
```
1. Dijkstra starts at $A$: `distances = {A:0, B:inf, C:inf}`. Min-Heap: `[(0, A)]`.
2. Pop `(0, A)`. Check neighbors of $A$:
   - $B$ is reached at distance 3. Push `(3, B)`.
   - $C$ is reached at distance 4. Push `(4, C)`.
   - `distances` is now `{A:0, B:3, C:4}`.
3. Pop the minimum element, which is `(3, B)`. Dijkstra now declares $B$ **finalized** at distance 3.
4. Pop the next minimum element, which is `(4, C)`. Dijkstra checks neighbors of $C$:
   - Edge $C \rightarrow B$ has weight $-2$.
   - New distance to $B$ is $4 + (-2) = 2$.
   - Since $2 < 3$, `distances[B]` updates to 2.
5. **The Failure**: Because $B$ was already popped and finalized, any paths stemming *from* $B$ were computed using the incorrect distance of 3, leading to incorrect shortest-path results for subsequent nodes in the graph.

---

## 3. The Bellman-Ford Algorithm

To solve shortest paths in the presence of negative edge weights (and to detect negative cycles), we use the **Bellman-Ford Algorithm**.

### The Principle of Relaxation
Instead of greedily selecting the minimum distance vertex, Bellman-Ford takes a brute-force dynamic programming approach. It **relaxes** all edges in the graph simultaneously, repeating this process $V - 1$ times.

> **Why $V-1$ times?**
> A shortest path in a graph containing $V$ vertices without cycles can contain at most $V - 1$ edges. In the worst case, each round of relaxation propagates the correct shortest-path distance along one additional edge of the path. Therefore, $V - 1$ iterations are mathematically sufficient to find all shortest paths.

### Negative Cycle Detection
A **negative cycle** is a loop in a graph whose total edge weight sum is negative:
```text
      (X) --( 2 )--> (Y)
       ^              /
        \--( -5 )----/
```
If a negative cycle exists, we can traverse it infinitely to make the path distance arbitrarily negative ($-\infty$). Thus, a defined "shortest path" does not exist.

Bellman-Ford detects this by running a **$V$-th iteration**:
- If we relax all edges one more time (on the $V$-th pass) and any distance decreases:
  $$\text{distances}[u] + \text{weight} < \text{distances}[v]$$
- Then that edge must be part of, or reachable from, a negative cycle.

### Complexity Analysis
- **Time Complexity**: $O(V \cdot E)$. We loop $V$ times and check all $E$ edges in each iteration.
- **Space Complexity**: $O(V)$ to store the shortest path distances.

---

## 4. The Floyd-Warshall Algorithm (All-Pairs Shortest Paths)

If we need to find the shortest path between **every pair of vertices** $(u, v)$ in a graph, running Dijkstra from every node takes $O(V^2 \log V + V \cdot E \log V)$ time. Running Bellman-Ford from every node takes $O(V^2 \cdot E)$ time.

The **Floyd-Warshall Algorithm** computes all-pairs shortest paths in $O(V^3)$ time using Dynamic Programming.

### The Recurrence Relation
Let $dp[k][i][j]$ be the shortest path from vertex $i$ to vertex $j$ using only intermediate vertices from the subset $\{1, 2, \dots, k\}$.
- To compute $dp[k][i][j]$, we have two choices:
  1. We do not use vertex $k$ as an intermediate node. The cost remains $dp[k-1][i][j]$.
  2. We do use vertex $k$ as an intermediate node. The path goes from $i \rightarrow k \rightarrow j$, costing $dp[k-1][i][k] + dp[k-1][k][j]$.
- **State Transition**:
  $$dp[k][i][j] = \min\Big(dp[k-1][i][j], \; dp[k-1][i][k] + dp[k-1][k][j]\Big)$$

### Space Complexity Compression Proof
The naive state space requires $O(V^3)$ memory to store the three dimensions. However, we can drop the $k$ dimension entirely and update a single 2D grid $dp[i][j]$ in-place, compressing space to $O(V^2)$.

#### Mathematical Proof of In-Place Correctness:
We must prove that updating $dp[i][j]$ in-place does not overwrite values from step $k-1$ that are needed later in step $k$.

Looking at the recurrence relation, to update $dp[i][j]$ at step $k$, we require:
1. The cell itself: $dp[i][j]$ (from step $k-1$)
2. The row component: $dp[i][k]$ (from step $k-1$)
3. The column component: $dp[k][j]$ (from step $k-1$)

What happens to $dp[i][k]$ when we update it at step $k$?
$$dp[i][k] \leftarrow \min(dp[i][k], \; dp[i][k] + dp[k][k])$$
Since the shortest path from vertex $k$ to itself ($dp[k][k]$) is $0$ (assuming no negative cycles), this simplifies to:
$$dp[i][k] \leftarrow \min(dp[i][k], \; dp[i][k] + 0) = dp[i][k]$$
The value of $dp[i][k]$ remains exactly the same during step $k$. Symmetrically, $dp[k][j]$ also remains unchanged.

Because the row and column components containing intermediate vertex $k$ are invariant during step $k$, updating the 2D grid in-place does not introduce race conditions or data corruption. The $O(V^2)$ space implementation is mathematically sound.

---

## 5. Disjoint Set Union (DSU) & Amortized Complexity

The Disjoint Set Union (DSU) (or Union-Find) data structure maintains a collection of disjoint sets, supporting two core operations:
1. `find(x)`: Return the representative element of the set containing `x`.
2. `union(x, y)`: Merge the set containing `x` with the set containing `y`.

To prevent DSU trees from degenerating into linear chains (which would make operations take $O(N)$ time), we apply two optimizations:

### 1. Union by Rank (or Size)
When merging two sets, we always attach the root of the shallower tree (smaller rank) to the root of the deeper tree (larger rank).
- This keeps the maximum height of any tree bounded by $O(\log N)$.

### 2. Path Compression
During a `find(x)` operation, we recursively traverse up to find the root. On the way back down, we update the parent pointer of *every node visited* to point directly to the root.
- This flattens the tree dynamically, ensuring subsequent lookups are extremely fast.

```text
     Before Path Compression:            After Path Compression (find(4)):
             (1)                                       (1)
            /   \                                    / / \ \
          (2)   (5)                                (2)(3)(4)(5)
          /
        (3)
        /
      (4)
```

### Amortized Complexity & The Inverse Ackermann Function
When combining **Union by Rank** and **Path Compression**, the worst-case time complexity of performing $M$ operations on a set of $N$ elements is:
$$O(M \cdot \alpha(N))$$
Where $\alpha(N)$ is the **Inverse Ackermann function**. 

The Ackermann function $A(x, y)$ grows extremely fast:
- $A(1, 1) = 3$
- $A(2, 2) = 7$
- $A(3, 3) = 61$
- $A(4, 4) \approx 2^{2^{2^{65536}}} - 3$ (a number far larger than the number of atoms in the observable universe)

Because the Ackermann function grows incredibly fast, its inverse function $\alpha(N)$ grows **incredibly slowly**. For any practical input size $N$ (up to $N < 10^{600}$):
$$\alpha(N) < 5$$
As a result, DSU operations run in **almost constant time $O(1)$ amortized** in practice, though the strict mathematical bound remains $O(\alpha(N))$.

---

## 6. DAGs & Topological Sorting

A Directed Acyclic Graph (DAG) is a directed graph with no directed cycles. DAGs are used to model dependencies where tasks must occur in a specific sequence.

A **Topological Sort** of a DAG is a linear ordering of its vertices such that for every directed edge $u \rightarrow v$, vertex $u$ comes before vertex $v$ in the ordering.

### Kahn's Algorithm (BFS-based)
Kahn's algorithm utilizes the concept of **In-Degree** (the number of incoming edges pointing to a vertex).
1. Calculate the in-degree of all vertices.
2. Initialize a Queue and enqueue all vertices with an in-degree of $0$ (nodes with no dependencies).
3. While the Queue is not empty:
   - Dequeue a vertex $u$ and append it to the topological order list.
   - For each outgoing edge $u \rightarrow v$:
     - Decrement the in-degree of $v$ by 1.
     - If the in-degree of $v$ becomes $0$, enqueue $v$.
4. **Cycle Detection**: If the final topological order list does not contain all vertices of the graph, the graph contains a cycle (a circular dependency loop).

### DFS-based Topological Sort
An alternative method uses DFS traversal:
1. Run DFS starting from unvisited nodes.
2. For a node $u$, recursively visit all its unvisited neighbors first.
3. Once all descendants of $u$ are fully explored, **push $u$ onto a Stack**.
4. The final topological order is obtained by popping elements from the Stack (reversing the finish order).

*Complexity*: Both topological sorting algorithms run in linear time:
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V)$
