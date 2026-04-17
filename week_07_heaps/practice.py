import heapq

# Exercise 1: MinHeap Implementation
# You are given a partial implementation of a MinHeap backed by an array.
# Implement the sift_up and sift_down mechanisms that restore the heap property.
class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, i): return (i - 1) // 2
    def get_left_child_index(self, i): return 2 * i + 1
    def get_right_child_index(self, i): return 2 * i + 2

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap root with the last element
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_up(self, index):
        # TODO: While the current element is smaller than its parent, swap them.
        pass

    def _sift_down(self, index):
        # TODO: While the current element is larger than either of its children, 
        # swap it with the SMALLEST of the two children.
        pass


# Exercise 2: Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# MUST complete in O(N log K) time. (Sorting the array takes O(N log N) which is too slow for massive arrays)
def find_kth_largest(nums: list, k: int) -> int:
    # TODO: Use Python's built-in `heapq` module to maintain a Min-Heap of size K.
    pass


if __name__ == "__main__":
    mh = MinHeap()
    for num in [5, 1, 9, 3, 2]:
        mh.push(num)
    
    print("MinHeap Pop:", mh.pop()) # Expect 1
    print("MinHeap Pop:", mh.pop()) # Expect 2

    nums = [3,2,1,5,6,4]
    k = 2
    print(f"{k}th largest element:", find_kth_largest(nums, k)) # Expect 5
