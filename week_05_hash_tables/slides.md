---
marp: true
theme: default
paginate: true
---

# Week 5: Hash Tables & Sets
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Hash Functions
2. Arrays as Maps
3. Hash Collisions
4. Lookup Time Complexity

---

# 1. Hash Maps: The Magic $O(1)$
- Hash Tables (Python dictionaries) provide $O(1)$ lookup, insertion, and deletion.
- Far faster than $O(N)$ arrays or $O(\log N)$ perfectly balanced trees.

---

# 2. How Hash Functions Work
Under the hood, a Hash Map is just a sparse standard array!
1. Pass the string key into a deterministic **Hash Function**. (e.g., `hash("apple") -> 108340`)
2. Modulo that massive number by the capacity of the array. ($108340 \pmod{10} = 0$).
3. Place the `value` at array index `0`.

To retrieve "apple", you run the math again and instantly check index `0`.

---

# 3. Hash Collisions
What happens when `hash("banana") \pmod{10}` also equals `0`?
- **Chaining**: Index 0 now holds a Linked List instead of a flat value. Walk the chain to find "banana".
- **Open Addressing**: If index 0 is full, check index 1. If 1 is full, check 2. 

If too many collisions occur, our $O(1)$ hash table degrades into an $O(N)$ Linked List! Good hash functions are critical.
