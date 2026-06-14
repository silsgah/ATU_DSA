# Solution Guide: Graphs I (Fundamentals)

This document contains the complete answers and step-by-step solutions to all conceptual, tracing, and modeling questions in the Week 8 Workbook (`questions.pptx`).

---

## Part 1: Conceptual Questions

### Question 1: Space Complexity Trade-offs
* **Scenario**: $V = 10^7$ (10 million users), $E = 1.5 \times 10^9$ (1.5 billion undirected friendships).

1. **Adjacency Matrix Space**:
   * An adjacency matrix of size $V \times V$ requires $V^2$ entries.
   * $V^2 = (10^7)^2 = 10^{14}$ cells.
   * At 1 byte per cell, this is $10^{14}$ bytes.
   * $10^{14} \text{ bytes} \approx 100 \times 10^{12} \text{ bytes} = \mathbf{100 \text{ Terabytes (TB)}}$ of memory.
   * *Conclusion*: This is completely impractical for standard computer memory.

2. **Adjacency List Space**:
   * An adjacency list has space complexity of $O(V + E)$.
   * Specifically, we store $V$ keys in a hash map, and for each key, a list of its neighbors. In an undirected graph, the sum of neighbor elements in all lists combined is $2E = 3.0 \times 10^9$ entries.
   * Total storage elements = $V + 2E = 10^7 + 3.0 \times 10^9 \approx 3.01 \times 10^9$ items.
   * At 8 bytes per reference/pointer, this requires $\approx 3.01 \times 10^9 \times 8 \text{ bytes} = 2.4 \times 10^{10} \text{ bytes} \approx \mathbf{24 \text{ Gigabytes (GB)}}$ of memory.

3. **Representation Choice**:
   * The **Adjacency List** is the only viable choice. 24 GB of RAM can easily fit on a single modern high-spec server, whereas 100 TB of RAM is prohibitively expensive and requires massive distributed storage systems. Real-world social networks are highly sparse (most users are only connected to a tiny fraction of the total user base), making adjacency matrices extremely wasteful.

---

### Question 2: Traversal Properties
1. **BFS Shortest Path Guarantee**:
   * BFS explores nodes level by level (nodes at distance 1, then distance 2, etc.). Because it always processes shorter paths before longer ones, the first time it reaches any node, it is guaranteed to have taken the shortest path (in terms of edge count).
   * DFS, on the other hand, plunges as deep as possible down a single path. It might reach a target node via a highly roundabout route before backtracking and finding a shorter one.
   * *Counter-example Graph*: Let $A$ connect to $B$ and $C$. Let $B$ connect to $D$, and $C$ connect to $D$ directly. Let there also be an edge directly from $A$ to $D$.
     ```
          B
        /   \
       A --- D
        \   /
          C
     ```
     If we search for path from $A$ to $D$:
     * **BFS**: Explores $A$'s neighbors ($B, C, D$). It finds $D$ immediately at distance 1 (Path: $A \rightarrow D$).
     * **DFS**: Might plunge through $B$ first. From $B$, it goes to $D$. It finds $D$ at distance 2 (Path: $A \rightarrow B \rightarrow D$), which is sub-optimal.

2. **When to Choose DFS over BFS**:
   * **Cycle Detection**: DFS is naturally suited for identifying cycles (back-edges) in directed/undirected graphs.
   * **Topological Sorting**: Dependency resolution (e.g. build tools, task order) is resolved using DFS exit/finish times.
   * **Pathfinding/Maze Solving (when any path is fine)**: DFS uses much less memory than BFS on deep, narrow graphs since it only stores the current path on the call stack, whereas BFS stores entire front layers in the queue.

---

### Question 3: The Visited Set Failure
* **Forget Visited in BFS**:
   * The queue will continuously append neighbors. In a cycle (e.g., $A \leftrightarrow B$), $A$ will queue $B$, then $B$ will queue $A$ again, infinitely.
   * Since BFS is iterative, it will not stack-overflow but will rapidly allocate memory for infinite elements in the queue, eventually causing an **Out Of Memory (OOM) crash**.
* **Forget Visited in DFS**:
   * The recursive function will call itself infinitely (e.g., `dfs(A)` calls `dfs(B)`, which calls `dfs(A)`).
   * This immediately fills up the execution stack. In Python, this will trigger a `RecursionError: maximum recursion depth exceeded` (typically capped at 1000). In other compiled languages, it causes a **Stack Overflow segment fault**.

---

## Part 2: Hand-Simulation Exercises

### Exercise 1: BFS Hand-Trace (Start A)
Neighbors processed in alphabetical order:

| Step | Pop Node | Queue (Front to Back) | Visited Set |
|------|----------|-----------------------|-------------|
| 0    | (Start)  | `['A']`               | `{'A'}`     |
| 1    | `A`      | `['B', 'C']`          | `{'A', 'B', 'C'}` |
| 2    | `B`      | `['C', 'D', 'E']`     | `{'A', 'B', 'C', 'D', 'E'}` |
| 3    | `C`      | `['D', 'E', 'F']`     | `{'A', 'B', 'C', 'D', 'E', 'F'}` |
| 4    | `D`      | `['E', 'F']`          | `{'A', 'B', 'C', 'D', 'E', 'F'}` |
| 5    | `E`      | `['F']`               | `{'A', 'B', 'C', 'D', 'E', 'F'}` |
| 6    | `F`      | `['G']`               | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 7    | `G`      | `[]`                  | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |

---

### Exercise 2: DFS Hand-Trace (Start A)
Neighbors visited in alphabetical order:

| Step | Action | Call Stack (Bottom to Top) | Visited Set |
|------|--------|----------------------------|-------------|
| 0    | (Start) | `[dfs(A)]` | `{'A'}` |
| 1    | Call `dfs(B)` | `[dfs(A), dfs(B)]` | `{'A', 'B'}` |
| 2    | Call `dfs(D)` | `[dfs(A), dfs(B), dfs(D)]` | `{'A', 'B', 'D'}` |
| 3    | Return `dfs(D)` | `[dfs(A), dfs(B)]` | `{'A', 'B', 'D'}` |
| 4    | Call `dfs(E)` | `[dfs(A), dfs(B), dfs(E)]` | `{'A', 'B', 'D', 'E'}` |
| 5    | Call `dfs(F)` | `[dfs(A), dfs(B), dfs(E), dfs(F)]` | `{'A', 'B', 'D', 'E', 'F'}` |
| 6    | Call `dfs(C)` | `[dfs(A), dfs(B), dfs(E), dfs(F), dfs(C)]` | `{'A', 'B', 'C', 'D', 'E', 'F'}` |
| 7    | Return `dfs(C)` | `[dfs(A), dfs(B), dfs(E), dfs(F)]` | `{'A', 'B', 'C', 'D', 'E', 'F'}` |
| 8    | Call `dfs(G)` | `[dfs(A), dfs(B), dfs(E), dfs(F), dfs(G)]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 9    | Return `dfs(G)` | `[dfs(A), dfs(B), dfs(E), dfs(F)]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 10   | Return `dfs(F)` | `[dfs(A), dfs(B), dfs(E)]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 11   | Return `dfs(E)` | `[dfs(A), dfs(B)]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 12   | Return `dfs(B)` | `[dfs(A)]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |
| 13   | Return `dfs(A)` | `[]` | `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` |

---

## Part 3: Real-World Modeling Challenges

1. **Google Maps Navigation**:
   * **Vertices**: Cities, intersections, or GPS coordinate nodes.
   * **Edges**: Road segments connecting vertices.
   * **Properties**: **Directed** (models one-way streets) and **Weighted** (weight represents road length, speed limits, or live traffic travel time).

2. **LinkedIn Network**:
   * **Vertices**: User profiles.
   * **Edges**: Mutual connections.
   * **Properties**: **Undirected** (connections are mutual/symmetric) and **Unweighted** (all connections are equal).

3. **Academic Course Prerequisites**:
   * **Vertices**: Academic course modules.
   * **Edges**: Prerequisites.
   * **Properties**: **Directed** (you must take Course A before Course B) and **Unweighted** (represents a dependency condition, not a cost).

4. **Web Search Crawler**:
   * **Vertices**: Webpages (URLs).
   * **Edges**: Hyperlinks within those pages pointing to other pages.
   * **Properties**: **Directed** (Page A links to Page B, but Page B might not link back) and **Unweighted**.

---

## Part 4: Coding Extensions (Conceptual Solutions)

1. **Path Reconstruction**:
   * To reconstruct the path, maintain a parent map `parent = {}`. When you queue or recurse to a `neighbor` from the current `node`, record `parent[neighbor] = node`. Once you reach the target, backtrack using `parent[target]` until you reach the start node, then reverse the collected path.

2. **Cycle Detection (DFS)**:
   * During traversal, pass the `parent` node into your recursive calls: `dfs(neighbor, current_node)`. If a `neighbor` is already in the `visited` set and `neighbor != parent`, it means we reached an already visited node through a different branch, indicating a cycle.

3. **Connected Components Count**:
   * Loop through all nodes of the graph. If a node is not visited, launch a full BFS/DFS from it. When that traversal returns, all nodes in its connected island will have been marked as visited. Increment your component count, then proceed to check the next unvisited node.
