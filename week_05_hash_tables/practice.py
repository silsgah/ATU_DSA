# Exercise 1: Build a Hash Map (Chaining Implementation)
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        # We start with a prime number of buckets to help distribute data evenly
        self.capacity = 1009
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        # We can use python's built in hash to turn anything to an int, 
        # then fit it to our buckets
        return hash(key) % self.capacity

    def put(self, key, value):
        # TODO: Insert or update a Key-Value pair
        # 1. Get hash index
        # 2. Check if bucket is None; if so, create ListNode and place it
        # 3. Otherwise, traverse the list. If key exists, update value.
        # 4. If end of list reached without finding key, append new ListNode.
        pass

    def get(self, key):
        # TODO: Return the value to which the specified key is mapped, or -1 if no mapping.
        pass


# Exercise 2: Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
def can_construct(ransomNote: str, magazine: str) -> bool:
    # TODO: Solve in O(N + M) time using a dictionary/hash map to count letters
    pass


if __name__ == "__main__":
    hm = MyHashMap()
    hm.put("apple", 150)
    hm.put("banana", 200)
    print("Apple price:", hm.get("apple"))
    
    hm.put("apple", 160)
    print("Updated Apple price:", hm.get("apple"))
    
    print("Ransom note (a, b):", can_construct("a", "b")) # False
    print("Ransom note (aa, ab):", can_construct("aa", "ab")) # False
    print("Ransom note (aa, aab):", can_construct("aa", "aab")) # True
