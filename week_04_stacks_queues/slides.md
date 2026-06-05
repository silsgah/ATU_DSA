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

---

# 5. Amortized Analysis: The Potential Method
Amortized analysis estimates average cost of operations across a sequence:
- **Potential Method**: Define potential function $\Phi$ mapping data structure state to a real number.
- Amortized cost of the $i$-th operation:
  $$\hat{c}_i = c_i + \Phi_i - \Phi_{i-1}$$
- **Example (PUSH/MULTIPOP)**: Define $\Phi = s$ (stack size).
  - PUSH: $\hat{c} = 1 + (s + 1) - s = 2 = O(1)$.
  - MULTIPOP($k$): actual cost $m = \min(k, s)$.
    $$\hat{c} = m + (s - m) - s = 0 = O(1)$$
  - Both operations are $O(1)$ amortized!

---

# 6. Circular Queue State Differentiation
For a circular queue of capacity $C$:
- If empty and full both map to `front == rear`, we cannot tell them apart.
- **Buffer Strategy**: Allocate an array of size $C + 1$, leaving one slot empty.
  - **Queue Empty**: `front == rear`
  - **Queue Full**: `(rear + 1) % (C + 1) == front`
- This resolves state ambiguity without needing a separate count variable.
