from collections import deque

# Exercise 1: Number of Islands (DFS)
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands. An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically.
def num_islands(grid: list[list[str]]) -> int:
    # TODO: Iterate through every cell. 
    # If the cell is '1', increment island count, and launch a DFS to turn all connecting '1's into '0's.
    pass


# Exercise 2: Shortest Path in Unweighted Graph (BFS)
# You are given a graph represented as an adjacency list. Find the shortest path distance
# from the `start` node to the `target` node. Return the number of edges. If unreachable, return -1.
def shortest_path(graph: dict, start: str, target: str) -> int:
    # TODO: Implemented BFS using a Queue. Keep track of current distance via tuples (node, distance).
    # Remember to ignore already visited nodes!
    pass


if __name__ == "__main__":
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Number of islands:", num_islands(grid)) # Expect 3

    adj_list = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }
    
    print("Shortest path A to G:", shortest_path(adj_list, 'A', 'G')) # Expect 3 (A->C->F->G)
