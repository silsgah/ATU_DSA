import time

# Exercise 1: Identify the Big O
# Read the following functions and write their time and space complexity in comments above them.

# 1a.
def print_first_element(arr):
    if len(arr) > 0:
        print(arr[0])

# Time Complexity: O(?)
# Space Complexity: O(?)

# 1b.
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Time Complexity: O(?)
# Space Complexity: O(?)

# 1c.
def tricky_loop(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])
    for j in range(100):
        print(j)

# Time Complexity: O(?)
# Space Complexity: O(?)


# Exercise 2: Code Optimization
# The following function checks if there are any duplicate elements in an array.
# Currently, it runs in O(N^2) time.
# Rewrite the function below it (optimized_has_duplicates) to run in O(N) time.

def bad_has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False

def optimized_has_duplicates(arr):
    # TODO: Implement this in O(N) time and O(N) space.
    pass


# Exercise 3: Profiling script
# Complete this function to evaluate how long `bad_has_duplicates` takes vs your `optimized_has_duplicates`
def time_execution():
    test_array = [i for i in range(10000)]
    test_array.append(5000) # One duplicate

    # Profile bad implementation
    start_time = time.time()
    # bad_has_duplicates(test_array)
    end_time = time.time()
    print(f"Bad Implementation took: {end_time - start_time} seconds")

    # Profile optimized implementation
    start_time = time.time()
    # optimized_has_duplicates(test_array)
    end_time = time.time()
    print(f"Optimized Implementation took: {end_time - start_time} seconds")

if __name__ == '__main__':
    time_execution()
