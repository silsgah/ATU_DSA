---
marp: true
theme: default
paginate: true
---

# Week 3: Linked Lists
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Concept of Nodes and Pointers
2. Singly vs Doubly Linked Lists
3. Important Patterns: Fast & Slow Pointers
4. Pointer manipulation

---

# 1. Nodes and Pointers
Unlike Arrays (one contiguous block of memory), Linked Lists are scattered objects in the heap memory pointing to each other.
- **Object**: Node
- **Contains**: `Data` payload and a `Next` pointer.
- **Access**: Random access is $O(N)$. Accessing `index[5]` requires starting at the head and walking 5 pointers.

---

# Arrays vs Linked Lists
- **Arrays**: $O(1)$ access, $O(N)$ insert (due to shifting). Good for reading data.
- **Linked Lists**: $O(N)$ access, $O(1)$ insert/delete (just shuffle pointers). Good for rapidly modifying data that you've already found.

---

# 2. Key Algorithmic Patterns
- **Reversing a Linked List**: Classic interview question. You must maintain references to `Previous`, `Current`, and `Next` to avoid breaking the chain.
- **Cycle Detection**: What if a pointer loops back? Use Floyd's Cycle-Finding Algorithm.

---

# 3. Floyd's Algorithm (Tortoise & Hare)
- Place a SLOW pointer pointing to `next`.
- Place a FAST pointer pointing to `next.next`.
- If a cycle exists, the fast pointer will eventually traverse the loop and "lap" the slow pointer from behind. If they collide, there's a loop!
