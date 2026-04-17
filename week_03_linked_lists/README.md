# Week 03: Linked Lists

## 1. Concept: Nodes and Memory
Unlike Arrays, which allocate a single large block of contiguous memory, Linked Lists allocate memory independently for each element (called a Node). 

Each Node contains:
1. The **Data/Value**
2. A **Pointer** (reference) to the next Node in the list.

### Pros and Cons
- **Pros:** 
  - Inserting or deleting an element at a known arbitrary spot is $O(1)$. You just change where the pointers point.
  - They never need "resizing" and don't over-allocate unneeded memory.
- **Cons:** 
  - Random access takes $O(N)$ time. You cannot ask a linked list for `list[15]`. You must traverse from the beginning, following pointers to the 15th node.
  - Extra memory requirement for holding the pointers.

## 2. Types of Linked Lists
- **Singly Linked List:** Nodes only point `next`.
- **Doubly Linked List:** Nodes point both `next` and `prev`. Uses more space but allows traversing backward.
- **Circular Linked List:** The last element's `next` pointer loops back to the head of the list.

## 3. Important Algorithmic Patterns

### Tortoise and Hare (Fast and Slow Pointers)
A very powerful technique where two pointers track through the list at different speeds. 
If a linked list has a cycle (is circular incorrectly), a slow pointer moving 1 step at a time and a fast pointer moving 2 steps will eventually collide. This is **Floyd's Cycle-Finding Algorithm**.

### Reversing a Linked List
A classic interview question that tests your ability to juggle pointers without losing reference to the rest of the list.

## Practical Assignment (`practice.py`)
1. Build a Singly Linked List from scratch, complete with Append and Traversal functionalities.
2. Implement Linked List reversal manually.
3. Detect cycles using the Fast/Slow pointer pattern.
