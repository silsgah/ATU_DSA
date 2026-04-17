# Week 11: Dynamic Programming I

## 1. What is Dynamic Programming?
Dynamic Programming (DP) is simply **recursion with caching**. 
If a problem can be broken down into sub-problems (like Divide and Conquer), but those sub-problems *overlap* and are calculated repeatedly, DP is the solution to prevent exponential $O(2^N)$ runtime.

DP = Divide and Conquer + Memoization.

## 2. The Core Concept: Fibonacci
The classic Fibonacci algorithm: `fib(n) = fib(n-1) + fib(n-2)`.

If we run `fib(5)`:
- It calls `fib(4)` and `fib(3)`.
- `fib(4)` calls `fib(3)` and `fib(2)`.
Notice that `fib(3)` is being calculated multiple times! For a massive number like `fib(50)`, this overlap causes billions of redundant calculations.

### Memoization (Top-Down)
We create a Hash Map or Array cache. Before exploring a recursive branch, we check: "Have we calculated this before?". If yes, return the cached answer. If not, calculate it, and cache it before returning.
This converts Fibonacci from $O(2^N)$ time to $O(N)$ time.

### Tabulation (Bottom-Up)
Instead of starting at 50 and recursively drilling down to 0, start at 0 and build sequentially up to 50 in a simple `for` loop array.
Tabulation guarantees no Recursion Depth Exceeded errors or Stack memory overhead.

## Practical Assignment (`practice.py`)
1. Solve the "Climbing Stairs" problem (a Fibonacci variant) using Tabulation (Bottom-Up DP).
1. Solve the 1D DP "House Robber" problem.
