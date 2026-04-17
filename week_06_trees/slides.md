---
marp: true
theme: default
paginate: true
---

# Week 6: Trees and BTs
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. Tree Terminology
2. Binary Search Trees (BSTs)
3. Depth-First Traversals (Pre/In/Post)
4. Introduction to Logarithmic complexity

---

# 1. What is a Tree?
- Trees are non-linear data structures representing hierarchies.
- Linked Lists are effectively a "1D tree".
- **Root**: Topmost node.
- **Leaf**: A node with no children.

---

# 2. Binary Search Trees (BSTs)
- **Binary**: Each node has at most TWO children (Left, Right).
- **Search Property**: EVERYTHING in the Left subtree is smaller than the parent. EVERYTHING in the Right subtree is larger.
- This sorting property enables $O(\log N)$ search times. To find a node, you eliminate half the tree at every step down.

---

# 3. Depth-First Traversals
How do we mathematically visit every node?
- **Pre-Order (Node, Left, Right)**: Good for copying trees.
- **In-Order (Left, Node, Right)**: Prints a BST in perfectly sorted ascending order.
- **Post-Order (Left, Right, Node)**: Good for deleting trees (delete children before the parent).
