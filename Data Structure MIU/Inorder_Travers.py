def preorder(root):
    if root is not None:
        print(root.left)
        preorder(root.data)
        preorder(root.reght)
