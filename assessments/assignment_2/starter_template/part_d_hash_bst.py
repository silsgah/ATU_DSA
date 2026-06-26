# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part D: Hash Tables and Binary Search Trees
# Academic Year 2025/2026
#
# Instructions:
#   - Implement all TODO sections.
#   - Do NOT change class or function signatures.
#   - No external libraries permitted.
# ============================================================================


# ============================================================================
# D1 (3 Marks) — Written question
# Explain hash collisions and the two standard resolution strategies.
# ============================================================================

def d1_explanation():
    """
    Answer all three parts:
      1. What is a hash collision?
      2. How does Chaining resolve it? What is its worst-case lookup time?
      3. How does Open Addressing (Linear Probing) resolve it? Worst-case time?
    """
    # TODO: Replace this string with your full written answer.
    return """
    Hash collision definition: (your answer)

    Chaining:
        Description: (your answer)
        Worst-case lookup: O(?)

    Open Addressing / Linear Probing:
        Description: (your answer)
        Worst-case lookup: O(?)
    """


# ============================================================================
# SAMPLE DATA  (used in D2 and D3)
# ============================================================================

results = [
    (1001, 'A'), (1002, 'B'), (1003, 'A'), (1004, 'C'),
    (1005, 'B'), (1006, 'A'), (1007, 'F'), (1008, 'B'),
    (1009, 'C'), (1010, 'A'),
]


# ============================================================================
# D2 (5 Marks)
# Build a frequency report: how many students received each grade letter?
# All five grade letters ('A', 'B', 'C', 'D', 'F') must appear in the output
# even if no student received that grade (count = 0).
#
# Expected output for the sample data:
#   {'A': 4, 'B': 3, 'C': 2, 'D': 0, 'F': 1}
# ============================================================================

def grade_frequency_report(results):
    """
    Count how many students received each grade letter.

    Args:
        results (list[tuple]): List of (student_id, grade_letter) tuples.

    Returns:
        dict: Mapping {'A': int, 'B': int, 'C': int, 'D': int, 'F': int}.

    Time complexity:  O(?)
    Space complexity: O(?)
    """
    # TODO: Implement grade_frequency_report.
    pass


# ============================================================================
# D3 (4 Marks)
# Return a SORTED list of student IDs for students who received a given grade.
# Time complexity must be O(N log N).
#
# After your implementation, explain in the docstring why the time complexity
# is O(N log N) and NOT O(N), despite using a hash table for grouping.
# ============================================================================

def find_students_with_grade(results, grade):
    """
    Return a sorted list of student IDs who received the given grade.

    Args:
        results (list[tuple]): List of (student_id, grade_letter) tuples.
        grade   (str):         The grade letter to filter by (e.g. 'A').

    Returns:
        list[int]: Sorted list of matching student IDs.

    Time complexity: O(N log N)
    Why not O(N)?  (fill in your explanation here)
    """
    # TODO: Implement find_students_with_grade.
    pass


# ============================================================================
# BST NODE — provided, do not modify
# ============================================================================

class BSTNode:
    """A single node in a Binary Search Tree keyed on grade_score."""
    def __init__(self, student_id, grade_score):
        self.student_id  = student_id
        self.grade_score = grade_score
        self.left  = None
        self.right = None

    def __repr__(self):
        return f"BSTNode(id={self.student_id}, score={self.grade_score})"


# ============================================================================
# D4 (4 Marks)
# Implement recursive BST insertion.
# Nodes are ordered by grade_score (left < root < right).
# Ignore duplicate scores (do not insert if score already exists).
#
# Demonstrate by inserting these records in order and drawing the resulting tree:
#   (1001, 72), (1002, 55), (1003, 88), (1004, 60), (1005, 95), (1006, 48)
# ============================================================================

def insert(root, student_id, grade_score):
    """
    Recursively insert a new node into the BST.

    Args:
        root        (BSTNode | None): The current root of the subtree.
        student_id  (int):            ID of the student.
        grade_score (int):            Score used as the BST key.

    Returns:
        BSTNode: The (possibly new) root of the subtree after insertion.
    """
    # TODO: Implement recursive BST insertion.
    pass

# TODO: After implementing insert(), draw the resulting tree structure in a
# comment block here showing all six inserted nodes.
#
# Tree structure after inserting (1001,72),(1002,55),(1003,88),(1004,60),(1005,95),(1006,48):
#
#     (your drawing here)


# ============================================================================
# D5 (4 Marks)
# Implement in-order traversal as a GENERATOR FUNCTION using `yield`.
# Visiting left -> root -> right must produce nodes in ascending grade_score order.
#
# Explain in the docstring why in-order traversal produces sorted output in a BST.
# ============================================================================

def inorder_traversal(root):
    """
    Generator that yields (grade_score, student_id) tuples in ascending order.

    Args:
        root (BSTNode | None): Root of the BST (or subtree).

    Yields:
        tuple: (grade_score, student_id) in ascending order of grade_score.

    Why does in-order traversal produce sorted output?
    (fill in your explanation here)
    """
    # TODO: Implement using yield / yield from.
    pass


# ============================================================================
# D6 (5 Marks)
# Part 1: search — find a student_id by grade_score.
# Part 2: find_range — return all student_ids whose score falls in [low, high].
#
# After both implementations, write the time complexities in the docstrings
# and explain when H = O(log N) vs H = O(N).
# ============================================================================

def search(root, grade_score):
    """
    Search the BST for a node with the given grade_score.

    Args:
        root        (BSTNode | None): Root of the BST.
        grade_score (int):            The score to search for.

    Returns:
        int | None: The student_id if found, otherwise None.

    Time complexity: O(H) where H = ?
    When is H = O(log N)?  (explain)
    When is H = O(N)?      (explain)
    """
    # TODO: Implement recursive (or iterative) BST search.
    pass


def find_range(root, low, high):
    """
    Return all student_ids whose grade_score is in the inclusive range [low, high],
    in ascending order of grade_score.

    Args:
        root (BSTNode | None): Root of the BST.
        low  (int):            Lower bound (inclusive).
        high (int):            Upper bound (inclusive).

    Returns:
        list[int]: Sorted list of student_ids within the score range.

    Time complexity: O(H + K) where H = tree height, K = number of results.
    Hint: use BST pruning to avoid visiting unnecessary subtrees.
    """
    # TODO: Implement find_range with BST pruning.
    pass


# ============================================================================
# TEST HARNESS — do not modify
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Part D: Hash Tables and Binary Search Trees")
    print("=" * 60)

    # D1 — written explanation
    print("\n--- D1: Hash Collision Explanation ---")
    print(d1_explanation())

    # D2 — grade frequency report
    print("\n--- D2: Grade Frequency Report ---")
    freq = grade_frequency_report(results)
    print(f"  Result:   {freq}")
    expected_freq = {'A': 4, 'B': 3, 'C': 2, 'D': 0, 'F': 1}
    print(f"  Expected: {expected_freq}")
    print(f"  PASS: {freq == expected_freq}")

    # D3 — find students with grade
    print("\n--- D3: Students with Grade 'A' ---")
    a_students = find_students_with_grade(results, 'A')
    print(f"  Result:   {a_students}")
    print(f"  Expected: {[1001, 1003, 1006, 1010]}")
    print(f"  PASS: {a_students == [1001, 1003, 1006, 1010]}")

    print("\n--- D3: Students with Grade 'D' (none) ---")
    d_students = find_students_with_grade(results, 'D')
    print(f"  Result:   {d_students}")
    print(f"  Expected: []")
    print(f"  PASS: {d_students == []}")

    # D4 — BST insertion
    print("\n--- D4: BST Insertion ---")
    insertions = [(1001, 72), (1002, 55), (1003, 88),
                  (1004, 60), (1005, 95), (1006, 48)]
    bst_root = None
    for sid, score in insertions:
        bst_root = insert(bst_root, sid, score)
    print(f"  Root node: {bst_root}")
    print(f"  Expected root score: 72  PASS: {bst_root is not None and bst_root.grade_score == 72}")

    # D5 — in-order traversal
    print("\n--- D5: In-Order Traversal ---")
    traversal = list(inorder_traversal(bst_root) or [])
    expected_traversal = [(48, 1006), (55, 1002), (60, 1004),
                          (72, 1001), (88, 1003), (95, 1005)]
    print(f"  Result:   {traversal}")
    print(f"  Expected: {expected_traversal}")
    print(f"  PASS: {traversal == expected_traversal}")

    # D6 — search
    print("\n--- D6: search ---")
    search_tests = [(72, 1001), (48, 1006), (95, 1005), (99, None)]
    s_pass = True
    for score, expected_id in search_tests:
        result = search(bst_root, score)
        status = "PASS" if result == expected_id else f"FAIL (got {result})"
        print(f"  search(score={score}) -> {result}  [{status}]")
        if result != expected_id:
            s_pass = False
    print(f"  All search tests passed: {s_pass}")

    # D6 — find_range
    print("\n--- D6: find_range ---")
    range_tests = [
        (50, 75, [1002, 1004, 1001]),   # scores 55, 60, 72
        (80, 100, [1003, 1005]),        # scores 88, 95
        (0,  40,  []),                  # none in range
        (48,  48,  [1006]),             # exact match
    ]
    r_pass = True
    for lo, hi, expected_ids in range_tests:
        result_ids = find_range(bst_root, lo, hi) or []
        # Sort both for comparison since order may vary
        status = "PASS" if sorted(result_ids) == sorted(expected_ids) else \
                 f"FAIL (got {result_ids}, expected {expected_ids})"
        print(f"  find_range({lo}, {hi}) -> {result_ids}  [{status}]")
        if sorted(result_ids) != sorted(expected_ids):
            r_pass = False
    print(f"  All find_range tests passed: {r_pass}")
