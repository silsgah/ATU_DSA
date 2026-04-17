# Exercise 1: Node and Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # TODO: Implement append.
        # Handle the edge case where the list is empty (self.head is None)
        # Otherwise, traverse to the end and add a new Node.
        pass

    def print_list(self):
        # TODO: Implement print traversal.
        # Print elements sequentially
        pass


# Exercise 2: Reverse a Linked List
def reverse_linked_list(head):
    # TODO: Reverse the pointers of the linked list in-place.
    # Return the new head.
    # Hint: You need pointers for previous, current, and next nodes.
    pass


# Exercise 3: Detect Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Use O(1) space complexity.
def has_cycle(head):
    # TODO: Implement Floyd's Tortoise and Hare algorithm.
    pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Original list:")
    ll.print_list()

    # Reversing
    ll.head = reverse_linked_list(ll.head)
    print("Reversed list:")
    ll.print_list()

    # Cycle Testing
    node_a = Node(5)
    node_b = Node(6)
    node_c = Node(7)
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_b # Cycle!

    print("Has cycle?", has_cycle(node_a)) # Expect True
