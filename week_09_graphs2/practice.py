import heapq
from collections import deque

# Exercise 1: Dijkstra's Algorithm
# You are given a graph where keys are nodes and values are lists of tuples: (neighbor, weight)
# Return the shortest distance from start to target. If unreachable, return -1.
def dijkstra(graph, start, target):
    # TODO: Implement a Min-Heap based priority queue.
    # Keep track of distances to each node to avoid revisiting nodes with a worse path.
    pass

# Exercise 2: Course Schedule (Topological Sort)
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you 
# must take course b first if you want to take course a.
# Return true if you can finish all courses. Otherwise, return false. (Detect if a cycle exists!)
def can_finish_courses(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: Implement Kahn's Algorithm
    # 1. Build an adjacency list mapping prerequisite -> dependent
    # 2. Maintain an array tracking the `in-degree` of every course.
    # 3. Add any course with 0 in-degrees to a Queue.
    # 4. Process the queue, reducing in-degrees of neighbors. If neighbor hits 0, add to queue.
    pass


if __name__ == "__main__":
    # Graph representing cities and drive time
    weighted_graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    print("Shortest time from A to E:", dijkstra(weighted_graph, 'A', 'E')) # Expect 8 (A->C->B->D->E)

    prereqs = [[1,0], [2,1], [3,2]]
    print("Can finish?", can_finish_courses(4, prereqs)) # True
    
    cycle_prereqs = [[1,0], [0,1]]
    print("Can finish cyclic courses?", can_finish_courses(2, cycle_prereqs)) # False
