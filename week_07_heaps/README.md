# Week 07: Heaps and Priority Queues

## 1. What is a Heap?
A Heap (specifically a Binary Heap) is a special kind of Tree. However, unlike a Binary Search Tree ($O(\log N)$ search time), a Heap is optimized for one specific question: **What is the absolute largest (or smallest) item in this dataset?**

Heaps answer that question in $O(1)$ time. 
Retrieving & deleting that top item (and maintaining the heap property) takes $O(\log N)$ time.

### The Heap Property
- **Max-Heap:** The value of a parent node is always *greater than or equal to* the values of its children. The absolute maximum value is guaranteed to be at the root.
- **Min-Heap:** The value of a parent node is always *less than or equal to* the values of its children. The absolute minimum value is guaranteed to be at the root.

*Crucial Difference from BST:* In a heap, there is no guaranteed relationship between siblings (left child is not necessarily smaller than right child).

## 2. Array Representation
Because a Binary Heap is a *complete* tree (all levels are fully filled except possibly the last, which is filled left-to-right), we typically do not use Node classes with `left` and `right` pointers. 
Instead, we store the heap sequentially in a standard 1D Array!

For any node at index `i`:
- Its parent is at `(i - 1) // 2`
- Its left child is at `2 * i + 1`
- Its right child is at `2 * i + 2`

## 3. Priority Queues
A Priority Queue is an abstract data structure, and a Heap is the standard mathematical way to implement it.
Instead of FIFO (First In First Out), it's *Highest Priority First Out*.
- Operating systems use this to schedule CPU processes based on priority.
- Networking routers use this to process urgent packets.

## Practical Assignment (`practice.py`)
1. Implement the `bubble_up` (sift_up) and `sink_down` (sift_down) helper methods for an Array-based MinHeap.
2. Solve the "Find the Kth Largest Element" problem using Python's built-in `heapq` module.
