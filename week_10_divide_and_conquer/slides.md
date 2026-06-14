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

---

# 4. The Master Theorem & Extensions
For recurrences of the form $T(n) = a T(n/b) + f(n)$:
- Compares driving function $f(n)$ with $n^{\log_b a}$.
- **Generalized Case 2**: If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$:
  $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$
- **Example ($T(n) = 2T(n/2) + n \log n$)**:
  Here, $a=2, b=2 \implies n^{\log_2 2} = n^1$. Since $f(n) = n \log^1 n$, we have $k=1$.
  $$T(n) = \Theta(n \log^2 n)$$

---

# 5. Strassen's Matrix Multiplication Recurrence
Standard matrix multiplication of two $N \times N$ matrices requires 8 multiplications of size $N/2 \times N/2$ submatrices, taking $O(N^3)$ time.
- **Strassen's Trick**: Reduces multiplications from 8 to 7 using algebraic identities.
- **Recurrence Relation**:
  $$T(N) = 7 T(N/2) + O(N^2)$$
- Using Master Theorem ($a=7, b=2$, driving function is $O(N^2) \implies N^{\log_2 7} \approx N^{2.81}$):
  $$T(N) = \Theta(N^{\log_2 7}) \approx O(N^{2.81})$$
