class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.capacity = 1009
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
            return

        current = self.buckets[index]
        while True:
            # If the key already exists, simply update the value
            if current.key == key:
                current.value = value
                return
            # If we reach the end, append new key-value pair
            if current.next is None:
                current.next = ListNode(key, value)
                return
            current = current.next

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
            
        return -1


def can_construct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    
    # Counter is a specialized dictionary for counting hashes in python
    # This solves the problem extremely concisely.
    # Alternatively, you can iterate over magazine and manually build the dictionary mapping.
    
    mag_counts = Counter(magazine)
    
    for char in ransomNote:
        if mag_counts[char] > 0:
            mag_counts[char] -= 1
        else:
            return False
            
    return True

if __name__ == "__main__":
    hm = MyHashMap()
    hm.put("apple", 150)
    hm.put("banana", 200)
    print("Apple price:", hm.get("apple"))
    
    hm.put("apple", 160)
    print("Updated Apple price:", hm.get("apple"))
    
    print("Ransom note (a, b):", can_construct("a", "b")) # False
    print("Ransom note (aa, aab):", can_construct("aa", "aab")) # True
