def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the topmost element or assign a dummy value if stack is empty
            top_element = stack.pop() if stack else '#'
            
            # If the mapping for the closing bracket doesn't match the stack's top
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket
            stack.append(char)
            
    # Valid if stack is totally clear at the end
    return not stack

class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value: int) -> bool:
        if self._is_full():
            return False
            
        if self._is_empty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True

    def dequeue(self) -> bool:
        if self._is_empty():
            return False
            
        if self.head == self.tail: # Only one element was in the queue
            self.head = -1
            self.tail = -1
            return True
            
        self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
        if self._is_empty():
            return -1
        return self.queue[self.head]

    def _is_full(self) -> bool:
        return (self.tail + 1) % self.k == self.head

    def _is_empty(self) -> bool:
        return self.head == -1

if __name__ == '__main__':
    print("Is '[{()}]' valid?", is_valid_parentheses("[{()}]")) # True
    print("Is '[(])' valid?", is_valid_parentheses("[(])")) # False

    cq = MyCircularQueue(3)
    print("Enqueue 1:", cq.enqueue(1)) 
    print("Enqueue 2:", cq.enqueue(2)) 
    print("Enqueue 3:", cq.enqueue(3)) 
    print("Enqueue 4:", cq.enqueue(4)) 
    print("Dequeue:", cq.dequeue())    
    cq.enqueue(4)                      
    print("Front:", cq.Front())        
