import binarytree
from binarytree import convert
from binarytree import Node
#
root = Node(11)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.left.right = Node(10)
root.right.right = Node(25)
# root.right.left = Node(15)
# root.right.right = Node(25)
print(root)

def flatten(node, parent=None):
    if node is None: return parent, parent
    # if not node.right:
    #     return node, node

    lastnode_L = flatten(node.left, node)[1]
    if node.right:
        lastnode_R = flatten(node.right, node)[1]
    else:
        lastnode_R = node

    if node.left:
        left = node.left
        node.left = None
        lastnode_L.right = node
        if parent:
            if node == parent.left:
                parent.left = left
            elif node == parent.right:
                parent.right = left
    else:
        left = node
    if parent:
        return parent.left, lastnode_R
    else:
        return left, lastnode_R



root = flatten(root)[0]
print(root)