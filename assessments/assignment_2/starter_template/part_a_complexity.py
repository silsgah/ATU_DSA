# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part A: Algorithmic Complexity Analysis
# Academic Year 2025/2026
#
# Instructions:
#   - Answer questions A1 to A5 directly in the functions and docstrings below.
#   - For written/explanation questions, write your answer in the string returned
#     by the function (or as a clearly labelled print statement).
#   - Do NOT change the function signatures.
# ============================================================================


# --- Provided code for analysis (do not modify) ---

def algorithm_x(records, target):
    for i in range(len(records)):
        for j in range(i, len(records)):
            if records[i] + records[j] == target:
                return (i, j)
    return None


def algorithm_y(records, target):
    seen = {}
    for i, val in enumerate(records):
        complement = target - val
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
    return None


def algorithm_z(records):
    n = len(records)
    for i in range(1, n):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j] > key:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records


# ============================================================================
# A1 (4 Marks)
# Determine the worst-case time complexity of algorithm_x.
# Explain which part of the code drives the cost.
# ============================================================================

def a1_analysis():
    """
    Write your analysis here.
    Your answer should state the worst-case time complexity and explain WHY.

    Example format:
        Worst-case time complexity: O(?)
        Space complexity: O(?)
        Explanation: ...
    """
    # TODO: Replace this string with your full written answer.
    return """
    Worst-case time complexity: O(?)
    Space complexity: O(?)
    Explanation: (your justification here)
    """


# ============================================================================
# A2 (4 Marks)
# Determine the worst-case time complexity of algorithm_y.
# What data structure makes it faster? What is the space trade-off?
# ============================================================================

def a2_analysis():
    """
    Write your analysis here.
    """
    # TODO: Replace this string with your full written answer.
    return """
    Worst-case time complexity: O(?)
    Space complexity: O(?)
    Data structure that enables the speedup: (your answer)
    Space trade-off explanation: (your answer)
    """


# ============================================================================
# A3 (4 Marks)
# Identify algorithm_z by name.
# State its best-case and worst-case time complexities and the input that causes each.
# ============================================================================

def a3_analysis():
    """
    Write your analysis here.
    """
    # TODO: Replace this string with your full written answer.
    return """
    Algorithm name: (your answer)
    Best-case time complexity: O(?)   Input arrangement: (describe)
    Worst-case time complexity: O(?)  Input arrangement: (describe)
    """


# ============================================================================
# A4 (4 Marks)
# Complete the complexity comparison table for N = 1,000,000.
# Return a list of dicts, each with keys: 'complexity', 'operations', 'rank'.
# ============================================================================

def a4_table():
    """
    Fill in the approximate number of operations at N = 1,000,000
    and rank them from 1 (fastest) to 5 (slowest).
    """
    # TODO: Fill in each entry below.
    return [
        {"complexity": "O(1)",        "operations": "?",  "rank": "?"},
        {"complexity": "O(log N)",    "operations": "?",  "rank": "?"},
        {"complexity": "O(N)",        "operations": "?",  "rank": "?"},
        {"complexity": "O(N log N)",  "operations": "?",  "rank": "?"},
        {"complexity": "O(N^2)",      "operations": "?",  "rank": "?"},
    ]


# ============================================================================
# A5 (4 Marks)
# Implement an iterative Fibonacci that runs in O(N) time and O(1) space.
# Then write your explanation of why the naive recursive version is O(2^N).
# ============================================================================

def fibonacci_iterative(n):
    """
    Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
    Must run in O(N) time and O(1) space.
    Do NOT use recursion.
    """
    # TODO: Implement your iterative solution here.
    pass


def a5_explanation():
    """
    Explain why the naive recursive Fibonacci is O(2^N) and not O(N).
    """
    # TODO: Replace this string with your full written answer.
    return """
    Why naive recursion is O(2^N): (your explanation)
    How the iterative version achieves O(N) time and O(1) space: (your explanation)
    """


# ============================================================================
# TEST HARNESS — do not modify
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Part A: Algorithmic Complexity Analysis")
    print("=" * 60)

    print("\n--- A1 Analysis ---")
    print(a1_analysis())

    print("\n--- A2 Analysis ---")
    print(a2_analysis())

    print("\n--- A3 Analysis ---")
    print(a3_analysis())

    print("\n--- A4 Complexity Table ---")
    for row in a4_table():
        print(f"  {row['complexity']:15s} | ops: {str(row['operations']):20s} | rank: {row['rank']}")

    print("\n--- A5 Fibonacci ---")
    test_cases = [(0, 0), (1, 1), (6, 8), (10, 55)]
    all_pass = True
    for n, expected in test_cases:
        result = fibonacci_iterative(n)
        status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
        print(f"  fibonacci_iterative({n}) = {result}  [{status}]")
        if result != expected:
            all_pass = False
    print(f"\n  All Fibonacci tests passed: {all_pass}")
    print("\n--- A5 Explanation ---")
    print(a5_explanation())
