from collections import deque

def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(r, c):
        # Base case: if out of bounds or water, stop.
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
            
        # "Sink" the island piece so we don't visit it again
        grid[r][c] = '0'
        
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

def shortest_path(graph: dict, start: str, target: str) -> int:
    if start not in graph: return -1
    if start == target: return 0

    # Queue stores tuples of (current_node, distance_from_start)
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

if __name__ == "__main__":
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Number of islands:", num_islands(grid)) 

    adj_list = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }
    
    print("Shortest path A to G:", shortest_path(adj_list, 'A', 'G')) 
