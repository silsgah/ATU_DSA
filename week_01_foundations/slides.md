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

---

# Stack vs. Heap Memory Layout
How does a computer organize variables in memory?
- **Stack Memory**:
  - Stores function activation records (local variables, arguments, return addresses).
  - Managed automatically in a Last-In, First-Out (LIFO) order.
  - Extremely fast allocation/deallocation (simply shifting a stack pointer).
- **Heap Memory**:
  - Stores dynamically allocated objects (dynamic arrays, lists, graph nodes, tree nodes).
  - Managed explicitly by the programmer (C/C++) or a runtime garbage collector (Python/Java).
  - Slower allocation (requires searching for free space) and prone to fragmentation.

---

# 4. Asymptotic Rigor: Summation Bounds
To analyze sums of the form $f(n) = \sum_{i=1}^n i^d$ where $d > 0$, we bound the summation using integrals:
$$\int_{0}^{n} x^d dx \le \sum_{i=1}^n i^d \le \int_{1}^{n+1} x^d dx$$
Evaluating the integrals:
$$\frac{n^{d+1}}{d+1} \le f(n) \le \frac{(n+1)^{d+1} - 1}{d+1}$$
By the Squeeze Theorem, we get a tight bound of:
$$f(n) = \Theta(n^{d+1})$$

---

# 5. Mutual Recursion call Stack Space
Consider functions alternating calls (e.g. $A(n) \to B(n-1) \to A(\lfloor\frac{n-1}{2}\rfloor)$).
- Stack space is proportional to the maximum recursion depth.
- If one branch divides input size (e.g., halving), the input shrinks logarithmically overall.
- Max stack depth becomes $O(\log N)$ rather than linear $O(N)$ despite the step-decrement in $A$.
