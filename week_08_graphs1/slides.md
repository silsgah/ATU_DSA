---
marp: true
theme: default
paginate: true
---

# Week 8: Graphs I (Fundamentals)
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Introduction to Graphs
2. Vertices and Edges
3. Adjacency Lists vs Matrices
4. Breadth-First & Depth-First Search

---

# 1. Real World Networks
- A Tree is just a strict, directed, acyclic Graph.
- Graphs model almost everything: The Internet, Social Networks, Maps.
- A graph consists of **Vertices** (nodes) connected by **Edges** (lines).

---

# 2. Graph Terminology
- **Directed**: Edges are one-way streets.
- **Undirected**: Edges are two-way roads.
- **Weighted**: Edges have a cost to traverse them.
- **Acyclic**: Impossible to walk in a continuous loop.

---

# 3. Representing Graphs in Code
- **Adjacency List**: A Hash Map where the Key is a vertex and the Value is a List of neighbors. *(Ideal for most graphs)*
- **Adjacency Matrix**: A 2D grid matrix where a 1 means an edge exists. *(Ideal for dense graphs, but consumes $O(V^2)$ RAM).*

---

# 4. Traversals
- **Breadth-First Search (BFS)**: Uses a Queue. Explores neighbors first. Finds the shortest path in unweighted networks!
- **Depth-First Search (DFS)**: Uses a Stack (or Recursion). Explores deep before backtracking. Used to detect cycles or isolated islands.
