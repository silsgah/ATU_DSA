# Week 08: Graphs I (Fundamentals)

## 1. What is a Graph?
A tree is actually a very strictly formulated Graph. 
A Graph is a general data structure representing networks of nodes (called **Vertices**) connected by lines (called **Edges**). 

Graphs model almost everything in the real world:
- The Internet (pages are vertices, hyperlinks are edges)
- Social Networks (people are vertices, friendships are edges)
- Maps (cities are vertices, roads are edges)

## 2. Graph Terminology
*   **Directed vs Undirected:** Are edges one-way arrows, or two-way roads? (Twitter followers are directed, Facebook friends are undirected).
*   **Weighted vs Unweighted:** Do the edges have a cost/distance associated with them? (A map uses weighted edges for mileage).
*   **Acyclic vs Cyclic:** Can you travel along the edges and get stuck in a continuous loop? (Trees are acyclic).

## 3. Representing Graphs in Code
Because nodes can connect to *any* other node, we don't usually use left/right pointers. We use:

**Adjacency List (Common)**
A Dictionary/Hash Map where the Key is a vertex, and the Value is a List of adjacent vertices. Ideal for sparse graphs (few edges).
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    ...
}
```

**Adjacency Matrix**
A 2D Array / Grid of size $V \times V$ where a `1` at `matrix[i][j]` means an edge exists between vertex $i$ and $j$. Ideal for dense graphs or tracking specific weights easily, but consumes $O(V^2)$ memory space!

## 4. Traversals
**Breadth-First Search (BFS):** Explores all immediate neighbors first. Often used to find the *shortest path* in unweighted graphs. Requires a **Queue**.
**Depth-First Search (DFS):** Follows a path forward as far as possible before dead-ending and backtracking. Used to detect cycles or find isolated islands. Requires a **Stack** (or recursion).
*(Note: Because graphs can be cyclic, you must ALWAYS maintain a `visited` Set to avoid infinite loops).*

## Practical Assignment (`practice.py`)
1. Build a recursive DFS to count how many distinct "islands" exist in a grid.
2. Build an iterative BFS to find the shortest exit route in a maze.
