# Week 02: Arrays, Strings, and Pointers

## 1. Static vs. Dynamic Arrays

In systems languages like C/C++, a standard array is **static**. Its size is fixed at compile time or initialization.
- A static array of 5 integers allocates a contiguous block of exactly 5 integer spaces (e.g., $5 * 4 bytes = 20 bytes$).
- Looking up an element is extremely fast: `address + index * sizes_of_type`. ($O(1)$)

**Dynamic Arrays** (like Python's `list`, C++'s `std::vector`, Java's `ArrayList`) can grow in size.
How does it accomplish this if arrays must be contiguous blocks of memory?
1. It allocates a static array of a certain capacity.
2. When the internal capacity is reached and a new element is appended, the dynamic array will:
   - Allocate a *new* block of memory, usually double the size of the old one.
   - Copy all elements from the old array into the new one. ($O(N)$)
   - Free the old memory.

*Important Note:* Appending to a dynamic array is $O(1)$ *amortized*. Sometimes it triggers an $O(N)$ reshape, but on average across many appends, it behaves like $O(1)$.

## 2. Strings as Arrays

In many environments, Strings are simply arrays of characters contiguous in memory. Therefore, almost all array algorithmic patterns directly apply to string manipulation problems. 
Note: In Python and Java, strings are *immutable*. Whenever you modify a character in a string, the system actually allocates a brand new string and copies everything over. When doing heavy string manipulation, use a Character Array (`list` in Python) and join them at the end.

## 3. Two Pointers Pattern

One of the most essential patterns for arrays. Often, an algorithmic problem that seems to require $O(N^2)$ can be solved in $O(N)$ by iterating through the array using two pointers simultaneously.

**Common Scenarios:**
- Two pointers starting from opposite ends and moving towards the center (e.g., checking for palindromes, reversing arrays).
- Two pointers starting at the same end but moving at different speeds (Sliding window, slow/fast pointer).

## Practical Assignment (`practice.py`)

This week, you will complete the following 5 exercises:
1. **Dynamic Array Basics**: Implement the core functionality of a dynamic array from scratch using raw static arrays, including dynamic resizing (doubling capacity).
2. **Dynamic Array Deletion & Insertion**: Implement index-based element shifting (`insert`) and dynamic memory reclamation (`pop`, which shrinks the capacity to avoid wasting memory when elements are deleted).
3. **Two Sum II (Sorted Array)**: Find two numbers in a sorted array that sum to a target in O(N) time and O(1) space using two pointers.
4. **Valid Palindrome**: Determine if a string is a palindrome after stripping non-alphanumeric characters, in O(N) time and O(1) space using two pointers.
5. **Container With Most Water**: Find two vertical lines that enclose the maximum water area in O(N) time and O(1) space using two pointers.
