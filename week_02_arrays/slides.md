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

---

# 4. Custom Growth Factor Resizing Amortization
What if resizing is expensive, e.g. copying cost $C(N) = N \log_2 N$?
- Resizes happen at capacities that are powers of growth factor $\gamma$: $1, \gamma, \gamma^2, \ldots, \gamma^k \le N$.
- Copying cost at step $i$ is $C(\gamma^i) = i \gamma^i \log_2(\gamma)$.
- Summing resizing costs up to $k = \log_\gamma N$:
  $$\sum_{i=1}^k i \gamma^i \log_2(\gamma) \approx N \log_\gamma N \log_2(\gamma) = N \log_2 N$$
- Dividing by $N$ appends gives an amortized cost of $O(\log N)$ per append.

---

# 5. Two-Pointer Sorted Search Invariants
In Two Sum II (Sorted), if $A[\text{left}] + A[\text{right}] > \text{Target}$:
- Since $A$ is sorted, any element index $k > \text{left}$ has $A[k] \ge A[\text{left}]$, which guarantees $A[k] + A[\text{right}] > \text{Target}$.
- Thus, $A[\text{right}]$ cannot form a valid pair with *any* remaining candidate.
- We can safely decrement `right` without missing the target pair, preserving $O(N)$ correctness.
