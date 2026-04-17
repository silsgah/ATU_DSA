# Week 01: Foundations & Algorithm Analysis

## 1. Asymptotic Analysis (Big-O Notation)

Asymptotic analysis is the process of describing the efficiency of algorithms as their input size ($N$) grows towards infinity. We use these notations to communicate memory use and execution time without tying it to specific hardware latency.

### The Big Three

*   **Big-O ($O$) - Upper Bound:** The worst-case scenario. It answers: "What is the maximum amount of time this algorithm will take?" This is the most common notation used in industry.
*   **Big-Omega ($\Omega$) - Lower Bound:** The best-case scenario. It answers: "What is the absolute minimum time this algorithm could take?"
*   **Big-Theta ($\Theta$) - Tight Bound:** When both the upper bound and lower bound are the same (e.g., iterating through an entire array will always take linear time).

### Common Complexity Classes (from fastest to slowest)

1.  **$O(1)$ - Constant Time:** Accessing an array element by index `arr[5]`. The time does not depend on the input size.
2.  **$O(\log N)$ - Logarithmic Time:** Binary search. The input size is divided by a fraction at each step.
3.  **$O(N)$ - Linear Time:** A simple `for` loop over an array. Time grows linearly with the input size.
4.  **$O(N \log N)$ - Linearithmic Time:** Mergesort, Quicksort. Combining dividing algorithms with linear combination steps.
5.  **$O(N^2)$ - Quadratic Time:** Nested `for` loops. Bubble sort, insertion sort.
6.  **$O(2^N)$ - Exponential Time:** Recursive calculation of Fibonacci without memoization.
7.  **$O(N!)$ - Factorial Time:** Generating all permutations of a string.

## 2. Rules for Analyzing Big-O

1.  **Drop the Constants:** `$O(2N)` is just `$O(N)$`. A constant multiplier does not change the growth trajectory fundamentally.
2.  **Drop the Non-Dominant Terms:** `$O(N^2 + N)$` becomes `$O(N^2)$`. As `$N$` grows very large, the `$N^2$` term will overshadow the `$N$` term.
3.  **Different Inputs mean Different Variables:** A loop over array `A` followed by a loop over array `B` is `$O(A + B)$`, not `$O(N)$`.

## 3. Memory & Basic Data Types

While Python abstracts memory management away, in systems programming (like C/C++), you manage memory explicitly on the stack (fast, localized, limited) or the heap (slower, fragmented, larger). 

When evaluating spatial complexity, consider:
*   Primitive variables (int, float, char) use $O(1)$ space.
*   Arrays/Lists of length $N$ use $O(N)$ space.
*   The call stack during recursive functions occupies space in memory. Depth of recursion $D$ uses $O(D)$ space!

### Python Specifics
In Python, integers are not fixed size (like the 32-bit `int` in C++); they are variable-length objects. A simple integer in Python carries a memory overhead.

## Practical Assignment (`practice.py`)

In this week's practical exercise, you are tasked with analyzing the time complexities of various poorly written functions and optimizing one function down to $O(N)$ time.
