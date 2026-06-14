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

---

# 5. Floyd's Linear Time Heap Construction
Building a heap from an array bottom-up (calling `siftDown` from bottom-most parent to root) runs in $O(N)$ time:
- A complete binary tree of size $N$ has at most $\lceil N/2^{h+1} \rceil$ nodes at height $h$.
- The work per node is proportional to its height $h$:
  $$T(N) \le \sum_{h=0}^{\lfloor \log N \rfloor} h \frac{N}{2^{h+1}} \le \frac{N}{2} \sum_{h=0}^{\infty} \frac{h}{2^h} = O(N)$$
- This is strictly faster than insertion-based top-down heap construction ($O(N \log N)$).

---

# 6. d-Ary Heaps
In a $d$-ary heap, each node has $d$ children instead of 2.
- Represents a flat 1-indexed array.
- For a node at index $i$, the parent and $j$-th child ($1 \le j \le d$) are mapped at:
  $$\text{Parent}(i) = \lfloor \frac{i - 2}{d} \rfloor + 1$$
  $$\text{Child}(i, j) = d \cdot (i - 1) + j + 1$$
- Decreasing key takes $O(\log_d N)$ operations (fewer levels), while deleting min/max takes $O(d \log_d N)$ due to finding the smallest child out of $d$ children.
