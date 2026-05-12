"""
Merge Sort — Priority Scheduling
=================================
STUDENT IMPLEMENTATION FILE

Implement merge sort to order Task objects by composite key:
  1. Primary:   priority  (ascending — lower number = higher priority)
  2. Secondary: deadline  (ascending — earlier deadline first)

The Task class already defines __lt__ so you can compare with  <  and  <=.

Rules:
  - Do NOT use sorted(), .sort(), or any built-in sorting.
  - Add Time / Space complexity comments above each function.
"""


# -----------------------------------------------------------------
# Time:  O(?)    Space: O(?)
# -----------------------------------------------------------------
def merge_sort(tasks: list) -> list:
    """
    Sort a list of Task objects using the merge sort algorithm.

    Parameters
    ----------
    tasks : list[Task]
        Unsorted list of tasks.

    Returns
    -------
    list[Task]
        A NEW sorted list (do not mutate the input).
    """
    # TODO: Implement merge sort
    #   1. Base case: lists of length 0 or 1 are already sorted.
    #   2. Divide: split the list into two halves.
    #   3. Conquer: recursively sort each half.
    #   4. Combine: merge the two sorted halves using the merge() helper.
    pass


# -----------------------------------------------------------------
# Time:  O(?)    Space: O(?)
# -----------------------------------------------------------------
def merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into one sorted list.

    Parameters
    ----------
    left : list[Task]
        First sorted half.
    right : list[Task]
        Second sorted half.

    Returns
    -------
    list[Task]
        Merged, sorted list.
    """
    # TODO: Implement the merge step
    #   - Use two index pointers (i for left, j for right).
    #   - Compare left[i] and right[j] using <= (uses Task.__lt__).
    #   - Append the smaller to the result.
    #   - After one side is exhausted, extend with the remainder.
    pass


# -----------------------------------------------------------------
# BONUS (5 marks)
# Time:  O(?)    Space: O(?)
# -----------------------------------------------------------------
def merge_sort_counted(tasks: list) -> tuple:
    """
    Sort tasks using merge sort AND count total comparisons.

    Parameters
    ----------
    tasks : list[Task]

    Returns
    -------
    (sorted_list, comparison_count) : tuple[list[Task], int]
    """
    # TODO (BONUS): Implement a version that tracks how many
    # element comparisons were made during the entire sort.
    # This lets you empirically verify O(N log N).
    pass


# -----------------------------------------------------------------
# Quick sanity check
# -----------------------------------------------------------------
if __name__ == "__main__":
    from task import Task

    tasks = [
        Task(1, "Write report",     3, 100, 5),
        Task(2, "Fix bug",          1, 50,  2),
        Task(3, "Code review",      2, 80,  3),
        Task(4, "Deploy to prod",   1, 30,  4),
        Task(5, "Team standup",     3, 90,  1),
    ]

    print("Before sorting:")
    for t in tasks:
        print(f"  {t}")

    sorted_tasks = merge_sort(tasks)

    print("\nAfter merge sort:")
    if sorted_tasks:
        for t in sorted_tasks:
            print(f"  {t}")
    else:
        print("  (merge_sort returned None — not yet implemented)")

    # Bonus
    result = merge_sort_counted(tasks)
    if result:
        sorted_t, count = result
        print(f"\nBonus: {count} comparisons to sort {len(tasks)} tasks")
