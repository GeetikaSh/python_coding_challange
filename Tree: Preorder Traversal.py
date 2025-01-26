def preOrder(root):
    # Base case: if the root is None, return
    if root is None:
        return
    
    # Print the current node's value
    print(root.info, end=" ")
    
    # Recursively traverse the left subtree
    preOrder(root.left)
    
    # Recursively traverse the right subtree
    preOrder(root.right)
