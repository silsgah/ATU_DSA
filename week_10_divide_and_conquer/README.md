# Week 10: Divide and Conquer

## 1. Core Principle
"Divide and Conquer" is an algorithmic paradigm based on recursion. The strategy is to:
1. **Divide** the problem into a number of smaller subproblems.
2. **Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner (the Base Case).
3. **Combine** the solutions to the subproblems into the solution for the original problem.

## 2. Famous Examples

### Binary Search
Perhaps the most famous D&C algorithm. To find a target in a sorted array, you don't iterate front-to-back. You check the middle number. 
1. **Divide:** If the middle number is too big, discard the right half. If it's too small, discard the left.
2. **Conquer/Combine:** Recursively binary search the remaining half until found.
*Time Complexity: $O(\log N)$*

### Merge Sort
A fast sorting algorithm.
1. **Divide:** Split the array into two halves until arrays have 1 element remaining.
2. **Conquer:** Sort the halves (an array of 1 is already sorted!)
3. **Combine:** Merge the small sorted arrays back together sequentially.
*Time Complexity: $O(N \log N)$*

### Quick Sort
Another sorting algorithm.
1. **Divide:** Pick a "pivot" element. Move everything smaller than the pivot to its left, and everything larger to its right.
2. **Conquer:** Recursively run Quick Sort on the left side and the right side.
3. **Combine:** No real combination step needed, sorting happened in place.
*Time Complexity: $O(N \log N)$ average, but $O(N^2)$ worst case.*

## Practical Assignment (`practice.py`)
1. Implement Binary Search.
2. Implement Merge Sort.
