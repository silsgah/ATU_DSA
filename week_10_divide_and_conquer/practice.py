# Exercise 1: Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. 
# Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.
def binary_search(nums: list[int], target: int) -> int:
    # TODO: Implement left and right pointers.
    # While left <= right, find mid point. If mid point is target, return it.
    # Otherwise shrink the window.
    pass


# Exercise 2: Merge Sort
# Implement the merge sort algorithm.
def merge_sort(arr: list[int]) -> list[int]:
    # TODO: Base case: if length <= 1, return arr
    # Divide step: Split arr into `left_half` and `right_half`
    # Conquer step: recursive call merge_sort on the halves
    # Combine step: merge the two sorted halves back together in ascending order
    
    # Write a helper function for the merge step
    pass


def merge(left: list[int], right: list[int]) -> list[int]:
    # TODO: Take two sorted arrays and merge them into one sorted array in O(N) time.
    pass


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    print("Find 9 index:", binary_search(nums, 9)) # Expect 4
    print("Find 2 index:", binary_search(nums, 2)) # Expect -1

    unsorted_arr = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted array:", merge_sort(unsorted_arr)) # Expect [3, 9, 10, 27, 38, 43, 82]
