---
marp: true
theme: default
paginate: true
---

# Week 11: Dynamic Programming I
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Dynamic Programming Definition
2. Fibonacci Example
3. Top-Down (Memoization)
4. Bottom-Up (Tabulation)

---

# 1. What is DP?
- **Dynamic Programming = Recursion + Caching**.
- If a recursive tree makes the *exact same* function calls multiple times (overlapping subproblems), you are wasting massive CPU time.
- Standard recursive Fibonacci is $O(2^N)$ time. With DP, it drops instantly to $O(N)$.

---

# 2. Memoization (Top-Down)
- Create a Hash Map / Array cache.
- Before computing `fib(N)`, ask: "Does `N` exist in the cache?"
- If yes, return the cached value immediately. If no, compute it, save it straight to the cache, then return.

---

# 3. Tabulation (Bottom-Up)
- Why risk "Maximum Recursion Depth" errors at all?
- Instead of starting at $N$ and recursing down to 0, use a simple `for` loop array.
- Start at 0, compute 1 from 0, compute 2 from 0 and 1, etc., up to $N$.
- Massively space-efficient and completely bypasses the call stack.
