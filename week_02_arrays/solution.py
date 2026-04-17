import ctypes

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
        
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


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

def reverse_string(chars):
    left = 0
    right = len(chars) - 1
    
    while left < right:
        # Swap characters in-place
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    
    print("Custom array internal capacity:", arr._capacity) # Should show 16 

    print("Two sum result:", two_sum_sorted([1, 2, 7, 11, 15], 9)) # Expect [2, 7]

    hw_chars = ["h","e","l","l","o"]
    reverse_string(hw_chars)
    print("Reversed:", hw_chars)
