---
marp: true
theme: default
paginate: true
---

# Week 2: Arrays, Strings, and Pointers
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Static vs. Dynamic Arrays
2. Memory Allocation under the hood
3. The Two Pointers Algorithmic Pattern
4. Strings as Character Arrays

---

# 1. Static vs. Dynamic Arrays
- **Static Array (C/C++)**: A contiguous, pre-sized block of memory. Size is fixed at $N$.
- **Dynamic Array (Python `list`, Java `ArrayList`)**: Automatically resizes itself.
- **How Dynamic Resizing works**: When full, it allocates a NEW array of double the size ($2N$), copies the old elements over ($O(N)$), and drops the old array.
- Appending is $O(1)$ *amortized*.

---

# 2. Strings as Arrays
- Strings are functionally just arrays of characters.
- **Python / Java Note**: Strings are *immutable* here. Modifying a character allocates a completely new string in memory.
- If you need to heavily modify a string, convert it to a char array `['t','e','s','t']`, do the work, and `.join()` it back.

---

# 3. The Two Pointers Pattern
- Essential technique to reduce nested loop $O(N^2)$ brute forces into $O(N)$ linear time!
- **Opposite Ends**: Pointers at `[0]` and `[len-1]` moving towards the center (e.g., Palindrome check, Reversing).
- **Same End (Fast/Slow)**: Often called the Sliding Window or Hare/Tortoise.

---

# Practical Example
- **Two Sum II (Sorted)**: Start left and right. If the sum is too big, move the right pointer to a smaller number. If it's too small, move the left pointer to a bigger number. Takes only $O(N)$!
