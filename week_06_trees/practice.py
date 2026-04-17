class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # TODO: Insert values following BST property. Use iteration or recursion.
        pass

# Exercise 1: Inorder Traversal
# Return an array of the node values in In-Order traversal
def inorder_traversal(root):
    # TODO: Left, Node, Right
    pass

# Exercise 2: Preorder Traversal
def preorder_traversal(root):
    # TODO: Node, Left, Right
    pass

# Exercise 3: Lowest Common Ancestor
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
def lowest_common_ancestor(root, p, q):
    # TODO: Use the BST property to efficiently climb down the tree to find the split point.
    pass

if __name__ == "__main__":
    # Build Tree
    tree = BST()
    for v in [10, 5, 15, 2, 7, 12, 20]:
        tree.insert(v)

    # Validate output
    print("Inorder:", inorder_traversal(tree.root))   # Expect sorted: [2, 5, 7, 10, 12, 15, 20]
    print("Preorder:", preorder_traversal(tree.root)) 

    print("LCA of 2 and 7:", lowest_common_ancestor(tree.root, TreeNode(2), TreeNode(7)).val) # Expect 5
