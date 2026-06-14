import ctypes

# Exercise 1: Custom Dynamic Array
class DynamicArray:
    def __init__(self):
        self._count = 0           
        self._capacity = 1        
        self._array = self._make_array(self._capacity)
        
    def __len__(self):
        return self._count
        
    def __getitem__(self, index):
        if not 0 <= index < self._count:
            raise IndexError('Index out of bounds')
        return self._array[index]
        
    def append(self, element):
        # If capacity reached, double it
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
            
        self._array[self._count] = element
        self._count += 1
        
    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        
        # Copy data
        for i in range(self._count):
            new_array[i] = self._array[i]
            
        self._array = new_array
        self._capacity = new_capacity
        
    def pop(self):
        if self._count == 0:
            raise IndexError('pop from empty array')
        
        val = self._array[self._count - 1]
        self._array[self._count - 1] = None  # Clear reference to prevent memory leak
        self._count -= 1
        
        # Shrink capacity if size falls to 1/4 of capacity
        if 0 < self._count <= self._capacity // 4:
            new_cap = max(1, self._capacity // 2)
            if new_cap != self._capacity:
                self._resize(new_cap)
                
        return val

    def insert(self, index, element):
        if not 0 <= index <= self._count:
            raise IndexError('Index out of bounds')
            
        # Resize if full
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
            
        # Shift elements to the right
        for i in range(self._count, index, -1):
            self._array[i] = self._array[i - 1]
            
        self._array[index] = element
        self._count += 1

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


# Exercise 2: Two Sum II - Sorted Array
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1  # We need a bigger number
        else:
            right -= 1 # We need a smaller number
            
    return None


# Exercise 3: Reverse a String in-place
def reverse_string(chars):
    left = 0
    right = len(chars) - 1
    
    while left < right:
        # Swap characters in-place
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


# Exercise 4: Valid Palindrome (Two Pointers)
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True


# Exercise 5: Container With Most Water (Two Pointers)
def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_val = 0
    
    while left < right:
        width = right - left
        # The amount of water is constrained by the shorter boundary
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_val = max(max_val, current_area)
        
        # Move the pointer pointing to the shorter boundary inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_val


if __name__ == '__main__':
    # Test Dynamic Array basics
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print("Custom array internal capacity after appends:", arr._capacity) # Should show 16
    
    # Test pop
    val = arr.pop()
    print(f"Popped value: {val}, capacity after pop: {arr._capacity}") # 9, capacity 16
    for _ in range(7): # Pop down to length 2
        arr.pop()
    print("Array length:", len(arr), "capacity:", arr._capacity) # Length 2, capacity should shrink to 8 or 4 (since count=2 <= 16//4)
    
    # Test insert
    arr.insert(2, 99)
    print(f"Value at index 2 (should be 99): {arr[2]}, length: {len(arr)}")

    # Test Two Sum
    print("Two sum result:", two_sum_sorted([1, 2, 7, 11, 15], 9)) # Expect [2, 7]

    # Test Reverse
    hw_chars = ["h","e","l","l","o"]
    reverse_string(hw_chars)
    print("Reversed:", hw_chars)
    
    # Test Palindrome
    print("Is Palindrome:", is_palindrome("A man, a plan, a canal: Panama")) # Should be True
    print("Is Palindrome (False):", is_palindrome("race a car")) # Should be False
    
    # Test Max Area
    print("Max Area:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) # Should be 49
