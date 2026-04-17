# Week 05: Hash Tables & Sets

## 1. What is a Hash Table?
Also known as Hash Maps or Dictionaries (in Python). A Hash Table aims to provide $O(1)$ lookup, insertion, and deletion for Key-Value pairs. This is significantly faster than searching an array ($O(N)$) or even searching a perfectly balanced binary tree ($O(\log N)$).

## 2. Core Mechanics
Under the hood, a Hash Table is just a very sparse contiguous array. To put a key into this array:
1. We run the string key through a **Hash Function**. The mathematical hash function deterministically converts the text string into a massive integer (e.g., `hash("apple") -> 98127398127`).
2. We modulo that huge number by the size of our underlying array (e.g., $98127398127 \pmod{10} = 7$).
3. We place our Key-Value pair into index 7 of our array.

When we need to look up "apple", we hash it again, mod it again, go straight to index 7, and say "Aha! There it is." ($O(1)$).

## 3. Collisions
What happens if "banana" also mods down to index 7? This is called a **Hash Collision**.
There are two main strategies:
1. **Chaining (Open Hashing):** Index 7 no longer holds just one value; it holds a Singly Linked List. We walk the linked list to find "banana" vs "apple". If our hash function is poor, all items cluster at one index, degrading our $O(1)$ Hash Table into an $O(N)$ Linked List.
2. **Open Addressing (Linear/Quadratic Probing):** Array holds standard values. If 7 is taken, we look at index 8. If 8 is taken, we look at 9, and put "banana" there. During lookup, if index 7 isn't "banana", we keep walking forward until we find it or hit an empty space.

## Practical Assignment (`practice.py`)
1. Implement a Hash Table from scratch using Array storage and chaining.
2. Use Python's built-in dictionaries (which use Open Addressing in modern versions!) to solve an interview algorithm problem fast.
