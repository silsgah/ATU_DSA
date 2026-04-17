---
marp: true
theme: default
paginate: true
---

# Week 9: Graphs II (Advanced)
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Algorithms for Weighted Graphs
2. Dijkstra's Algorithm
3. Directed Acyclic Graphs (DAGs)
4. Topological Sorting

---

# 1. The Shortest Path Problem
- Standard BFS works perfectly to find the fastest route if all roads take exactly 1 minute.
- Standard BFS completely fails if you are using Google Maps with highways and slow side-streets.
- We need an algorithm that explores based on accumulated time/distance, not hop count.

---

# 2. Dijkstra's Algorithm 
- Uses a **Min-Heap (Priority Queue)** instead of a standard FIFO queue.
- At every step, it pops off the known location with the absolute shortest accumulated distance from the start point.
- Because of the Min-Heap, the *first* time we hit our target destination, we are mathematically guaranteed it's the fastest route.

---

# 3. Topological Sort (DAGs)
- What if a graph represents university course prerequisites? (Must take 101 before 201).
- We can sort this dependency tree into a linear list using Kahn's Algorithm.
- If we can't complete the sort, the Graph has a cycle (e.g. 101 requires 201 and 201 requires 101), indicating a deadlock!
