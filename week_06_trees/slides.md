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
- **Pre-Order (Node, Left, Right)**: Good for copying/printing trees.
- **In-Order (Left, Node, Right)**: Prints a BST in perfectly sorted ascending order.
- **Post-Order (Left, Right, Node)**: Good for deleting trees or postfix expressions.

---

# 4. AVL Trees & Balance Recurrences
An AVL Tree maintains balance: the heights of any node's two subtrees differ by at most 1.
- Let $N(h)$ be the minimum number of nodes in an AVL tree of height $h$.
- **Recurrence**: $N(h) = N(h-1) + N(h-2) + 1$
- **Base cases**: $N(0) = 1$, $N(1) = 2$
- **Example ($h=3$)**:
  $$N(2) = N(1) + N(0) + 1 = 2 + 1 + 1 = 4$$
  $$N(3) = N(2) + N(1) + 1 = 4 + 2 + 1 = 7$$
- This guarantees height $h = O(\log N)$.

---

# 5. Recursive Diameter Complexity
The diameter is the longest path between any two nodes in a tree.
- A naive recursive approach computes `height(left)` and `height(right)` at each node:
  $$T(N) = T(\text{left}) + T(\text{right}) + O(\text{height})$$
- For a highly unbalanced linear tree of size $N$, this requires:
  $$T(N) = \sum_{i=1}^N O(i) = O(N^2)$$
- *Optimization*: Return height and diameter together in a single bottom-up $O(N)$ pass.
