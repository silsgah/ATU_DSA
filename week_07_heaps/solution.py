import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, i): return (i - 1) // 2
    def get_left_child_index(self, i): return 2 * i + 1
    def get_right_child_index(self, i): return 2 * i + 2
    def has_parent(self, i): return self.get_parent_index(i) >= 0
    def has_left_child(self, i): return self.get_left_child_index(i) < len(self.heap)
    def has_right_child(self, i): return self.get_right_child_index(i) < len(self.heap)

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_up(self, index):
        # Bubble the element UP until it is larger than its parent
        while self.has_parent(index) and self.heap[self.get_parent_index(index)] > self.heap[index]:
            parent_idx = self.get_parent_index(index)
            # Swap
            self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
            index = parent_idx

    def _sift_down(self, index):
        # Bubble the element DOWN until it is smaller than both children
        while self.has_left_child(index):
            smaller_child_idx = self.get_left_child_index(index)
            
            # If right child exists and is EVEN SMALLER than left child, use right
            if (self.has_right_child(index) and 
                self.heap[self.get_right_child_index(index)] < self.heap[smaller_child_idx]):
                smaller_child_idx = self.get_right_child_index(index)
                
            # If the current element is already smaller than the smallest child, stop
            if self.heap[index] < self.heap[smaller_child_idx]:
                break
                
            # Otherwise, swap and continue
            self.heap[index], self.heap[smaller_child_idx] = self.heap[smaller_child_idx], self.heap[index]
            index = smaller_child_idx


def find_kth_largest(nums: list, k: int) -> int:
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # If the heap exceeds size K, pop the smallest element.
        # This means the heap will only ever contain the K absolute largest elements seen so far.
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # The root of the MinHeap (index 0) will be the kth largest overall.
    return min_heap[0]


if __name__ == "__main__":
    mh = MinHeap()
    for num in [5, 1, 9, 3, 2]:
        mh.push(num)
    
    print("MinHeap Pop:", mh.pop()) # Expect 1
    print("MinHeap Pop:", mh.pop()) # Expect 2

    nums = [3,2,1,5,6,4]
    k = 2
    print(f"{k}th largest element:", find_kth_largest(nums, k)) # Expect 5
