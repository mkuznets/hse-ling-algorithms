def flatten(root):
    if root:
        flatten(root.right)
        if root.left:
            flatten(root.left)
            p = root.left
            while p.right is not None:
                p = p.right
            p.right, root.right, root.left = root.right, root.left, None
     else:
        return 
