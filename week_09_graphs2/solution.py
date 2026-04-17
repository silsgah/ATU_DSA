import heapq
from collections import deque

def dijkstra(graph, start, target):
    if start not in graph: return -1
    
    # Priority Queue stores tuples of (accumulated_distance, node)
    pq = [(0, start)]
    
    # Track the minimum distance found so far to each node
    min_distances = {node: float('infinity') for node in graph}
    min_distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # We reached the target! Since we use a Min-Heap, the FIRST time we naturally 
        # pop the target off the heap, it's guaranteed to be the shortest path.
        if current_node == target:
            return current_distance
            
        # Optimization: If we pulled off an outdated tuple that has a longer distance
        # than what we already know is possible, ignore it.
        if current_distance > min_distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            dist = current_distance + weight
            
            # If we found a strictly shorter path to this neighbor
            if dist < min_distances[neighbor]:
                min_distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
                
    return -1


def can_finish_courses(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1
        
    queue = deque()
    # Find all courses that require 0 prerequisites and can be taken immediately
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
            
    completed_courses = 0
    
    while queue:
        current = queue.popleft()
        completed_courses += 1
        
        # Taking this course fulfills a prerequisite for its neighbors
        for dependent_course in adj[current]:
            in_degree[dependent_course] -= 1
            # If the dependent course now has no remaining prereqs, add it to the queue
            if in_degree[dependent_course] == 0:
                queue.append(dependent_course)
                
    # If the number of completed courses equals the total, we didn't hit a cyclic deadlock
    return completed_courses == numCourses


if __name__ == "__main__":
    weighted_graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    print("Shortest time from A to E:", dijkstra(weighted_graph, 'A', 'E')) 

    prereqs = [[1,0], [2,1], [3,2]]
    print("Can finish?", can_finish_courses(4, prereqs)) 
    
    cycle_prereqs = [[1,0], [0,1]]
    print("Can finish cyclic courses?", can_finish_courses(2, cycle_prereqs)) 
