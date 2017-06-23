import binarytree
from binarytree import convert
from binarytree import Node
#
root = Node(10)
root.left = Node(6)
root.right = Node(11)
root.left.left = Node(5)
root.left.right = Node(7)
print(root)

def flatten(node):
    if node is None: return

    if node.right is None:
        node.lastnode = node
    if node.left is None:
        node.topnode = node

    flatten(node.left)
    flatten(node.right)

    if node.left:
        node.left.topnode.lastnode.right = node #делаем родителя node-a
        node.topnode = node.left.topnode
        if node.right:
            node.topnode.lastnode = node.right.lastnode
        else:
            node.topnode.lastnode = node
        node.left = None #стерли старую ссылку на левый узел

    return node.topnode

print(flatten(root))