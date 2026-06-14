import ctypes # Used to create raw C-style arrays in Python

# Exercise 1: Custom Dynamic Array
# We normally use Python lists which are dynamically resizing automatically.
# Here, you will build one from scratch using a static array.

class DynamicArray:
    def __init__(self):
        self._count = 0           # Count of actual elements
        self._capacity = 1        # Max capacity before resize
        self._array = self._make_array(self._capacity)
        
    def __len__(self):
        return self._count
        
    def __getitem__(self, index):
        if not 0 <= index < self._count:
            raise IndexError('Index out of bounds')
        return self._array[index]
        
    def append(self, element):
        # TODO: Implement append.
        # If the array is full, call self._resize(2 * self._capacity)
        pass
        
    def _resize(self, new_capacity):
        # TODO: Implement resize.
        # 1. create a new static array using self._make_array(new_capacity)
        # 2. copy items from the old array to the new array
        # 3. set self._array to point to the new array
        # 4. update self._capacity
        pass
        
    def pop(self):
        # TODO: Implement pop (removes and returns the last element).
        # 1. If array is empty, raise IndexError.
        # 2. Save the last element.
        # 3. Clear reference to prevent memory leaks: self._array[self._count - 1] = None
        # 4. Decrement count.
        # 5. Shrink capacity to half if self._count <= self._capacity // 4 (minimum capacity of 1).
        # 6. Return the saved element.
        pass

    def insert(self, index, element):
        # TODO: Implement insert(index, element).
        # 1. Check if index is valid (0 <= index <= self._count). If not, raise IndexError.
        # 2. If capacity is reached, double capacity by calling self._resize(2 * self._capacity).
        # 3. Shift all elements from index to self._count-1 to the right by one position.
        # 4. Insert element at index.
        # 5. Increment count.
        pass

    def _make_array(self, capacity):
        # Generates a static array structure (low level)
        return (capacity * ctypes.py_object)()


# Exercise 2: Two Sum II - Sorted Array
# Given an array SORTED in ascending order, find two numbers that add up to a specific target.
# You must do this in O(N) time and O(1) space! (No Hash Maps allowed!)
def two_sum_sorted(arr, target):
    # TODO: Implement using two pointers from opposite ends.
    pass


# Exercise 3: Reverse a String in-place
# Write a function that reverses a string. 
# The input string is given as an array of characters: ["h","e","l","l","o"].
# Must be solved in O(1) extra space.
def reverse_string(chars):
    # TODO: Implement in-place reversal
    pass


# Exercise 4: Valid Palindrome (Two Pointers)
# Given a string s, return True if it is a palindrome, or False otherwise.
# You must ignore non-alphanumeric characters and letter case.
# Solve it in O(N) time and O(1) extra space using two pointers.
# Example: "A man, a plan, a canal: Panama" -> True
def is_palindrome(s: str) -> bool:
    # TODO: Implement palindrome check.
    pass


# Exercise 5: Container With Most Water (Two Pointers)
# Given an array of non-negative integers height where height[i] represents a vertical line.
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum area of water.
# Solve in O(N) time and O(1) space using two pointers.
def max_area(height: list[int]) -> int:
    # TODO: Implement container area maximization.
    pass


if __name__ == '__main__':
    # Test Dynamic Array basics
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print("Array built! Length:", len(arr))
    
    # Test pop and insert (remove comments once implemented)
    # val = arr.pop()
    # print(f"Popped value: {val}, new length: {len(arr)}")
    # arr.insert(2, 99)
    # print(f"Inserted 99 at index 2. Value at index 2: {arr[2]}, length: {len(arr)}")

    # Test Two Sum
    print("Two Sum:", two_sum_sorted([1, 2, 7, 11, 15], 9)) # Should be (2, 7) or indices (1, 2)

    # Test Reverse
    hw_chars = ["h","e","l","l","o"]
    reverse_string(hw_chars)
    print("Reversed chars:", hw_chars)
    
    # Test Palindrome (remove comments once implemented)
    # print("Is Palindrome:", is_palindrome("A man, a plan, a canal: Panama")) # Should be True
    
    # Test Max Area (remove comments once implemented)
    # print("Max Area:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) # Should be 49
