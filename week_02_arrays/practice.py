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


if __name__ == '__main__':
    # Test Dynamic Array
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print("Array built! Length:", len(arr))

    # Test Two Sum
    print("Two Sum:", two_sum_sorted([1, 2, 7, 11, 15], 9)) # Should be (2, 7) or indices (1, 2)

    # Test Reverse
    hw_chars = ["h","e","l","l","o"]
    reverse_string(hw_chars)
    print("Reversed chars:", hw_chars)
