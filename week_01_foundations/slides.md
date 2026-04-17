---
marp: true
theme: default
paginate: true
---

# Week 1: Foundations & Algorithm Analysis
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Asymptotic Analysis (Big-O Notation)
2. Time vs. Space Complexity 
3. Memory and Basic Data Types (Hardware intuition)
4. Hands-on Profiling

---

# 1. Asymptotic Analysis
How do we talk about algorithm speed without worrying about CPU specs?
- **Big-O ($O$)**: Upper bound (Worst-case) - Our main focus in industry.
- **Big-Omega ($\Omega$)**: Lower bound (Best-case).
- **Big-Theta ($\Theta$)**: Tight bound (Exact scaling).

---

# Complexity Classes 
From fastest to slowest:
1. $O(1)$: Constant Time (Array access)
2. $O(\log N)$: Logarithmic Time (Binary Search)
3. $O(N)$: Linear Time (Standard loop)
4. $O(N \log N)$: Linearithmic (Merge/Quick Sort)
5. $O(N^2)$: Quadratic (Nested loops, Bubble Sort)
6. $O(2^N)$: Exponential (Naive Recursion)
7. $O(N!)$: Factorial (Permutations)

---

# 2. Golden Rules of Big-O
1. **Drop the Constants**: $O(2N)$ is simply $O(N)$.
2. **Drop Non-Dominant Terms**: $O(N^2 + N)$ -> The $N^2$ eclipses the $N$ as inputs grow towards infinity, so it's just $O(N^2)$.
3. **Use Different Variables for Different Inputs**: Looping through Array `A` then Array `B` is $O(A + B)$, not $O(N)$.

---

# 3. Space Complexity & Memory
- Time is only half the battle. How much memory (Space) does your algorithm require?
- In systems languages, memory is bounded tightly.
- Python abstracts this away, but integers and strings have memory overheads.
- **Warning**: Recursive functions use $O(D)$ space on the Call Stack where $D$ is the depth of the recursion!
