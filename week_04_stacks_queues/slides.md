---
marp: true
theme: default
paginate: true
---

# Week 4: Stacks and Queues
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Stacks (LIFO)
2. Queues (FIFO)
3. Limitations of Arrays for Queues
4. Circular Queues

---

# 1. Stacks
- **LIFO (Last-In, First-Out)**: Like a stack of plates.
- **Operations ($O(1)$)**: `push()`, `pop()`, `peek()`.
- **Uses**: The Call Stack (functions returning), Undo mechanisms, parsing syntax like `()[]{}`.
- Python lists make excellent Stacks natively.

---

# 2. Queues
- **FIFO (First-In, First-Out)**: Like a line at the grocery store.
- **Operations ($O(1)$)**: `enqueue()`, `dequeue()`.
- **Uses**: Task scheduling (printers, web APIs), Breadth-First Search.

---

# 3. Why Array Queues Fail
- If you use a basic Array as a Queue, `pop(0)` drops the first element. 
- *Problem*: You must shift every other element left by one slot to fill the gap. That makes Dequeueing an $O(N)$ operation!

---

# 4. Better Queue Solutions
- **Doubly Linked List**: Just point the `head` elsewhere. ($O(1)$)
- **Ring Buffer (Circular Queue)**: A static array with sliding `head` and `tail` pointers that wrap around the array's boundaries via modulo math. Highly memory efficient.
