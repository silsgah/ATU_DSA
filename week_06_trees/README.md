# Week 06: Trees and Basic Traversals

## 1. What is a Tree?
A tree is a non-linear data structure consisting of nodes connected by edges. It represents a hierarchical relationship. 
If Linked Lists are essentially 1D lines of nodes, Trees are nodes that branch out to zero or more child nodes.
- **Root:** The topmost node.
- **Leaf:** A node with no children.

## 2. Binary Trees & BSTs
A **Binary Tree** is a tree where any given node can have at most *two* children (Left and Right).
A **Binary Search Tree (BST)** enforces an important sorting property:
*   Everything in the Left subtree is smaller than the parent node.
*   Everything in the Right subtree is larger than the parent node.

Because of this property, looking up a number in a *balanced* BST takes $O(\log N)$ time. You start at the root; if your target is smaller, you exclusively search the left, eliminating half the tree instantly. 

## 3. Traversals (DFS vs BFS)
How do we mathematically visit every node in a tree?

**Depth First Search (DFS)** - Explore as deep as possible before backtracking.
Implemented recursively or via a Stack.
1. **Pre-Order** (Node, Left, Right): Good for creating a deep copy of a tree.
2. **In-Order** (Left, Node, Right): Good for reading data out of a BST in perfectly sorted ascending order.
3. **Post-Order** (Left, Right, Node): Good for deleting a tree, as you delete children before parents.

**Breadth First Search (BFS) / Level Order Traversal** - Explore level by level horizontally.
Implemented via a Queue.

## Practical Assignment (`practice.py`)
1. Implement the structure of a BST and insert data into it.
2. Write functions to traverse the tree In-Order and Pre-Order to understand how the order affects recursion output.
