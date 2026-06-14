from collections import deque

# Exercise 1: Build Adjacency List
# Given a list of undirected edges (pairs of nodes), build and return the 
# corresponding adjacency list (dictionary where keys are nodes and values are lists of neighbors).
# Example input: [('A', 'B'), ('A', 'C'), ('B', 'D')]
# Example output: {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
def build_adj_list(edges: list[list[str]]) -> dict[str, list[str]]:
    # TODO: Initialize dictionary. For each edge (u, v), add v to u's list and u to v's list.
    pass


# Exercise 2: Basic BFS Traversal Order
# Perform a standard Breadth-First Search (BFS) starting from `start_node`.
# Return a list of nodes visited in the order they were processed (popped from the queue).
def bfs_traversal(graph: dict[str, list[str]], start_node: str) -> list[str]:
    # TODO: Implement BFS. Keep track of processed nodes in a list to return.
    pass


# Exercise 3: Basic DFS Traversal Order
# Perform a standard Depth-First Search (DFS) starting from `start_node`.
# Return a list of nodes visited in the order they were first reached.
# Use recursion.
def dfs_traversal(graph: dict[str, list[str]], start_node: str) -> list[str]:
    # TODO: Implement recursive DFS.
    pass


# Exercise 4: Shortest Path in Unweighted Graph (BFS)
# You are given a graph represented as an adjacency list. Find the shortest path distance
# from the `start` node to the `target` node. Return the number of edges. If unreachable, return -1.
def shortest_path(graph: dict[str, list[str]], start: str, target: str) -> int:
    # TODO: Implement BFS using a Queue. Keep track of current distance via tuples (node, distance).
    pass


# Exercise 5: Number of Islands (DFS on a 2D Grid)
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands. An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically.
def num_islands(grid: list[list[str]]) -> int:
    # TODO: Iterate through every cell. 
    # If the cell is '1', increment island count, and launch a DFS to turn all connecting '1's into '0's.
    pass


if __name__ == "__main__":
    # Test Exercise 1
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F'), ('F', 'G')]
    graph = build_adj_list(edges)
    print("Exercise 1 - Built Graph:")
    if graph:
        for node, neighbors in sorted(graph.items()):
            print(f"  {node}: {neighbors}")
    else:
        print("  Not implemented yet.")

    print("\n--------------------")

    # Test Exercises 2 & 3
    # Using the graph generated above:
    print("Exercise 2 - BFS Traversal (Start A):", bfs_traversal(graph if graph else {}, 'A'))
    print("Exercise 3 - DFS Traversal (Start A):", dfs_traversal(graph if graph else {}, 'A'))

    print("\n--------------------")

    # Test Exercise 4
    print("Exercise 4 - Shortest Path A to G:", shortest_path(graph if graph else {}, 'A', 'G'))

    print("\n--------------------")

    # Test Exercise 5
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Exercise 5 - Number of islands:", num_islands(grid))
