---
marp: true
theme: default
paginate: true
---

# Week 10: Divide and Conquer
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Divide and Conquer Paradigm
2. Binary Search
3. Merge Sort
4. Quick Sort

---

# 1. The Core Principle
An algorithmic technique based heavily on recursion:
1. **Divide**: Break the problem into much smaller subproblems.
2. **Conquer**: Solve the subproblems. If small enough, just solve directly (Base Case).
3. **Combine**: Merge the solved subproblems together to form the final answer.

---

# 2. Binary Search
- The most famous D&C algorithm. ($O(\log N)$)
- **Divide**: Check the middle of a sorted array. If the target is smaller, permanently discard the right half.
- **Conquer**: Recurse on the remaining half.
- *Fun Fact*: Checking 4 billion sorted records takes at most 32 operations!

---

# 3. Merge Sort
- **Divide**: Split the array down the middle until arrays are length 1.
- **Conquer**: An array of size 1 is inherently sorted.
- **Combine**: Merge the tiny sorted arrays sequentially back together into larger sorted arrays. ($O(N \log N)$).
