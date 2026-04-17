class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
            
        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    return
                current = current.right


def inorder_traversal(root):
    res = []
    
    def dfs(node):
        if not node: return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
        
    dfs(root)
    return res

def preorder_traversal(root):
    res = []
    
    def dfs(node):
        if not node: return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    return res


def lowest_common_ancestor(root, p, q):
    current = root
    
    while current:
        if p.val > current.val and q.val > current.val:
            current = current.right
        elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
            return current # We found the split!

if __name__ == "__main__":
    tree = BST()
    for v in [10, 5, 15, 2, 7, 12, 20]:
        tree.insert(v)

    print("Inorder:", inorder_traversal(tree.root))   
    print("Preorder:", preorder_traversal(tree.root)) 

    print("LCA of 2 and 7:", lowest_common_ancestor(tree.root, TreeNode(2), TreeNode(7)).val) 
