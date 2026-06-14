from collections import deque

# Exercise 1: Build Adjacency List
def build_adj_list(edges: list[list[str]]) -> dict[str, list[str]]:
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = [] # {'A': []}
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph


# Exercise 2: Basic BFS Traversal Order
def bfs_traversal(graph: dict[str, list[str]], start_node: str) -> list[str]:
    if start_node not in graph:
        return []
    
    visited = {start_node}
    queue = deque([start_node])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


# Exercise 3: Basic DFS Traversal Order
def dfs_traversal(graph: dict[str, list[str]], start_node: str) -> list[str]:
    if start_node not in graph:
        return []
    
    visited = set()
    order = []
    
    def dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                
    dfs(start_node)
    return order


# Exercise 4: Shortest Path in Unweighted Graph (BFS)
def shortest_path(graph: dict[str, list[str]], start: str, target: str) -> int:
    if start not in graph or target not in graph: 
        return -1
    if start == target: 
        return 0

    queue = deque([(start, 0)]) 
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        
        if node == target:
            return dist
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return -1 # Target unreachable


# Exercise 5: Number of Islands (DFS on a 2D Grid)
def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
            
        grid[r][c] = '0' # Sink
        
        dfs(r + 1, c) # Down
        dfs(r - 1, c) # Up
        dfs(r, c + 1) # Right
        dfs(r, c - 1) # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                num_islands += 1
                dfs(r, c)
                
    return num_islands


if __name__ == "__main__":
    # Test Exercise 1
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F'), ('F', 'G')]
    graph = build_adj_list(edges)
    print("Exercise 1 - Built Graph:")
    for node, neighbors in sorted(graph.items()):
        print(f"  {node}: {neighbors}")

    print("\n--------------------")

    # Test Exercises 2 & 3
    print("Exercise 2 - BFS Traversal (Start A):", bfs_traversal(graph, 'A'))
    print("Exercise 3 - DFS Traversal (Start A):", dfs_traversal(graph, 'A'))

    print("\n--------------------")

    # Test Exercise 4
    print("Exercise 4 - Shortest Path A to G:", shortest_path(graph, 'A', 'G'))

    print("\n--------------------")

    # Test Exercise 5
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Exercise 5 - Number of islands:", num_islands(grid))
