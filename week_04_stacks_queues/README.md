# Week 04: Stacks and Queues

## 1. Stacks (LIFO)
**Last-In, First-Out.** Imagine a stack of plates; you add to the top and you remove from the top.

**Core Operations:**
- `push()`: Add an item to the top. $O(1)$
- `pop()`: Remove and return the top item. $O(1)$
- `peek()`: Look at the top item without removing it. $O(1)$

**Real World Uses:**
- Function call stack (recursion uses this under the hood).
- Undo functionality in text editors.
- Parsing syntax (like balanced parentheses or HTML tags).

**Implementation detail:** A Stack can easily be implemented using a Dynamic Array or a Singly Linked List.

## 2. Queues (FIFO)
**First-In, First-Out.** Imagine a line of people waiting for a cashier. The first person to arrive is the first to be served.

**Core Operations:**
- `enqueue()`: Add an item to the back of the queue. $O(1)$
- `dequeue()`: Remove and return the item from the front. $O(1)$

**Real World Uses:**
- Task scheduling (Printers, Web servers handling API requests).
- Breadth-First Search (BFS) in graph traversal.

**Implementation detail:** A standard Dynamic Array is TERRIBLE for a Queue. If you dequeue an element from index 0 of an array, every subsequent element must shift left to fill the gap, making it an $O(N)$ operation. 
Instead, Queues are usually implemented using a **Doubly Linked List** or a **Ring Buffer (Circular Array)**.

## Practical Assignment (`practice.py`)
1. Implement a Queue correctly using an underlying array structure (hint: you can't just `pop(0)`). Python provides `collections.deque` (Doubly Ended Queue) precisely because standard lists fail at FIFO efficiency. You will reconstruct to understand why.
2. Build a Parentheses Validator using a Stack.
