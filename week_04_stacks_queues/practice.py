# Exercise 1: Valid Parentheses (Stack)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# Valid means open brackets must be closed by the same type, and in the correct order.
def is_valid_parentheses(s):
    # TODO: Implement using a list as a Stack.
    # Python lists are excellent for stacks: append() and pop() operate on the end of the list.
    pass


# Exercise 2: Circular Queue
# Design your implementation of the circular queue. The circular queue is a linear data structure 
# in which the operations are performed based on FIFO (First In First Out) principle and the 
# last position is connected back to the first position to make a circle.
class MyCircularQueue:
    def __init__(self, k: int):
        # Initialize queue with maximum size K
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value: int) -> bool:
        # TODO: Insert an element into the circular queue. Return True if successful.
        pass

    def dequeue(self) -> bool:
        # TODO: Delete an element from the circular queue. Return True if successful.
        pass

    def Front(self) -> int:
        # TODO: Get the front item. Return -1 if queue is empty
        pass


if __name__ == '__main__':
    print("Is '[{()}]' valid?", is_valid_parentheses("[{()}]")) # True
    print("Is '[(])' valid?", is_valid_parentheses("[(])")) # False

    # Circular queue test
    cq = MyCircularQueue(3)
    print("Enqueue 1:", cq.enqueue(1)) # True
    print("Enqueue 2:", cq.enqueue(2)) # True
    print("Enqueue 3:", cq.enqueue(3)) # True
    print("Enqueue 4:", cq.enqueue(4)) # False
    print("Dequeue:", cq.dequeue())    # True
    cq.enqueue(4)                      # True
    print("Front:", cq.Front())        # Expect 2
