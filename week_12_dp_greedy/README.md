# Week 12: Dynamic Programming II & Greedy

## 1. 2D Dynamic Programming
In Week 11, the DP state tracked just *one* moving constraint (e.g., "what house am I at?"). That requires a 1D Array `dp[i]`.
In 2D DP, state is defined by *two* moving constraints simultaneously. This requires building a grid/matrix `dp[i][j]`.

**Classic Problem: The 0/1 Knapsack**
You are a thief with a backpack that can hold $W$ weight. You are in a room full of items, each with a different Weight and Value. You want to maximize Value without exceeding Weight limit $W$.
The two variables are:
1. Which subset of items am I looking at? (Index $i$)
2. How much weight capacity do I have remaining? (Weight $w$)
To solve this, we fill a matrix where traversing down processes a new item, and traversing right gives us more weight capacity.

## 2. Greedy Algorithms
A Greedy Algorithm is an algorithm that makes the absolute *locally optimal choice* at every step with the hope that these local choices will lead to a global optimum.
Unlike DP, Greedy algorithms DO NOT reconsider past decisions.

**Pros:** Extremely fast and simple to implement (usually $O(N \log N)$ due to sorting data first).
**Cons:** Unsafe. If picking a shiny object now prevents you from picking an even bigger shiny object later, Greedy will fail, but DP will succeed because DP explores all possibilities via recursion branches.

Greedy works for problems exhibiting the **Greedy Choice Property**, such as Fractional Knapsack or Interval Scheduling.

## Practical Assignment (`practice.py`)
1. Solve a classic 2D DP problem: Longest Common Subsequence.
2. Solve a Greedy scheduling problem: Assign Cookies.
