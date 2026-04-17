import time

# Exercise 1: Identify the Big O

# 1a.
# Time Complexity: O(1) - Because it only accesses one element regardless of array size.
# Space Complexity: O(1) - No extra scaling memory is allocated.
def print_first_element(arr):
    if len(arr) > 0:
        print(arr[0])


# 1b.
# Time Complexity: O(N^2) - Nested loop over the same array length N.
# Space Complexity: O(1) - Prints immediately, does not store pairs.
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# 1c.
# Time Complexity: O(N) - Loop runs N/2 times -> O(N). Second loop runs 100 times (constant, dropped).
# Space Complexity: O(1) - No extra variables allocated depending on N.
def tricky_loop(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])
    for j in range(100):
        print(j)


# Exercise 2: Code Optimization

def bad_has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False

def optimized_has_duplicates(arr):
    """
    By using a hash set, we achieve O(1) average lookup time.
    Overall Time Complexity: O(N) because we visit each element at most once.
    Overall Space Complexity: O(N) because worst-case we store all elements in the set.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


# Exercise 3: Profiling script
def time_execution():
    test_array = [i for i in range(10000)]
    test_array.append(5000) # One duplicate

    print("Starting profiling ...")
    
    start_time = time.time()
    bad_has_duplicates(test_array)
    end_time = time.time()
    print(f"Bad Implementation took: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    optimized_has_duplicates(test_array)
    end_time = time.time()
    print(f"Optimized Implementation took: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    time_execution()
