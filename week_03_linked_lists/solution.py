class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next # Save the next node
        current.next = prev      # Reverse the pointer
        
        # Shift the pointers forward
        prev = current
        current = next_node
        
    return prev # Prev becomes the new head at the very end


def has_cycle(head):
    if head is None or head.next is None:
        return False
        
    slow = head
    fast = head.next
    
    while slow != fast:
        # If fast reaches the end, there is no cycle
        if fast is None or fast.next is None:
            return False
            
        slow = slow.next          # Move 1 step
        fast = fast.next.next     # Move 2 steps
        
    return True # Collision occurred!

if __name__ == '__main__':
    ll = LinkedList()
    for i in range(1, 5):
        ll.append(i)
        
    print("Original:")
    ll.print_list()
    
    ll.head = reverse_linked_list(ll.head)
    print("Reversed:")
    ll.print_list()

    node_a = Node(5)
    node_b = Node(6)
    node_c = Node(7)
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_b
    print("Has cycle?:", has_cycle(node_a))
