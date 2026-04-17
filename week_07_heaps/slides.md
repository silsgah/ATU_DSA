---
marp: true
theme: default
paginate: true
---

# Week 7: Heaps & Priority Queues
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. What is a Heap?
2. Solving the "Max/Min" problem in $O(1)$
3. Arrays under the hood
4. Sift/Bubble operations

---

# 1. Binary Heaps
A Heap is a Tree perfectly optimized to answer one question: "What is the absolute largest/smallest item in this dataset?"
- **Min-Heap**: The parent is ALWAYS smaller than or equal to both its children. 
- The absolute minimum is guaranteed to be at the root. Retrieving it is $O(1)$!

---

# 2. Priority Queues
- Heaps implement the abstract **Priority Queue** data structure.
- Instead of First-In-First-Out, it's *Highest-Priority First-Out*.
- Essential for OS process scheduling or Network packet routing.

---

# 3. Array Representation
Heaps are *Complete* trees (filled perfectly top-to-bottom, left-to-right). Thus, they are practically implemented as flat 1D Arrays, not connected Nodes!
For an element at index `i`:
- Left child is at `2i + 1`
- Right child is at `2i + 2`
- Parent is at `(i - 1) // 2`

---

# 4. Real World Application
Finding the "K-th largest element" out of 100 Billion records.
Sorting takes $O(N \log N)$ and massive memory.
Using a Min-Heap capped at size $K$ takes only $O(N \log K)$ and uses minimal RAM.
