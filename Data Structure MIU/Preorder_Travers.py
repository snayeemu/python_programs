def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
