"""
For all the traversal algorithms (preorder, postorder and inorder, including complexity for is_bst methods) -
Time complexity - O(n) as each node is traversed exactly once
Space complexity - O(h) where h is the height of the BST

Both approaches use the recursion stack, values of h for eaxch case is -
1. Best Case (Balanced Tree): h = O(log n)
2. Worst Case (Skewed Tree): h = O(n)
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order(node):
    if node:
        print(node.value, end=" ")  # Visit root
        pre_order(node.left)       # Traverse left subtree
        pre_order(node.right)      # Traverse right subtree

def in_order(node):
    if node:
        in_order(node.left)        # Traverse left subtree
        print(node.value, end=" ") # Visit root
        in_order(node.right)       # Traverse right subtree

def post_order(node):
    if node:
        post_order(node.left)      # Traverse left subtree
        post_order(node.right)     # Traverse right subtree
        print(node.value, end=" ") # Visit root


def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    """
    Recursively checks if a binary tree is a BST.

    Args:
        node: The root of the binary tree.
        min_value: The minimum value a node can take (initially -infinity).
        max_value: The maximum value a node can take (initially infinity).

    Returns:
        bool: True if the tree is a BST, False otherwise.
    """
    if not node:
        return True
    
    # Check if the current node satisfies the BST property
    if not (min_value < node.value < max_value):
        return False

    # Check recursively for left and right subtrees
    return (is_bst(node.left, min_value, node.value) and
            is_bst(node.right, node.value, max_value))

def is_bst_in_order_traversal_check(node):
    """
    Explicitly checks if a binary tree is a BST by comparing node values directly.

    Args:
        node: The root of the binary tree.

    Returns:
        bool: True if the tree is a BST, False otherwise.
    """
    # Helper function for in-order traversal and validation
    def _check(node, last_visited):
        if not node:
            return True
        
        # Check the left subtree
        if not _check(node.left, last_visited):
            return False
        
        # This originates from the fact that in inorder traversal of a BST, the previous node is always smaller than next 
        if last_visited[0] is not None and node.value <= last_visited[0]:
            return False
        last_visited[0] = node.value
        
        # Check the right subtree
        return _check(node.right, last_visited)

    # Use a mutable object (list) to track the last visited node value
    return _check(node, [None])

def search(root, key):
    """
    Time complexity of search is O(h) which can be O(log n) in best case or O(n) in worst case
    Space complexity of search is again O(h) which depends on max recursion depth, again h
    """
    if root is None:
        return 
    else:
        if root.value == key:
            return root
        elif key > root.value:
            return search(root.right, key)
        else:
            return search(root.left, key)

def search_iterative(root, key):
    """
    Iterative search for a key in a Binary Search Tree
    Time complexity is O(h) and space complexity is O(1)
    """
    current = root
    while current:
        if current.value == key:  # Key found
            return current
        elif key > current.value:  # Key is greater, move to right subtree
            current = current.right
        else:  # Key is smaller, move to left subtree
            current = current.left
    return None  # Key not found

def insert_node(root, key):
    # Time complexity is O(h) and space complexity is O(1) as no recursion
    new = TreeNode(key)
    prev = None
    while root:
        prev = root
        if root.value == key:
            return
        elif key > root.value:
            root = root.right
        else:
            root = root.left
    if key > prev.value:
        prev.right = new
    else:
        prev.left = new
    return new

# Example usage:
if __name__ == "__main__":
    # Construct a sample tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    """ 
    Tree structure
          10
         /  \
        5    15
       / \     \
      2   7     20
    """

    # Check if the tree is a BST
    print("The tree is a BST:", is_bst(root))
    print("The tree is a BST:", is_bst_in_order_traversal_check(root))
    
    # Searching for a particular key
    key = 20
    result = search(root, key)
    if result:
        print(f"Searched key {key} found at node: {result}")
    
    # Insert a new node
    insert_node(root, 19)   
    in_order(root)
