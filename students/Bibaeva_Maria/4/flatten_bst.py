from binarytree import tree, bst, pprint, inspect, convert
my_bst = convert([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
pprint(my_bst)

class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        self.parent = None

def find_max(node):
    if node is None:
        return
    while node.right:
        node = node.right
    return node

def find_min(node):
    if node is None:
        return
    while node.left:
        node = node.left
    return node

def set_parents(node):
    if node is None:
        return
    if node.left:
        node.left.parent = node
        set_parents(node.left)
    if node.right:
        node.right.parent = node
        set_parents(node.right)

def flatten(node, min_node):
    if node is None:
        return
    root = None
    if node.left:
        l_node = node.left
        m_node = find_max(node.left)
        if m_node is not l_node:
            if node.parent is not None: 
                node.parent.right = l_node
                l_node.parent = node.parent
            else:
                l_node.parent = None
            m_node.right = node
            node.left = None
            flatten(l_node, min_node)
        elif m_node is l_node:
            if node.parent is not None:
                node.parent.right = m_node
                m_node.parent = node.parent
            else:
                node.parent = None
            m_node.right = node
            node.parent = m_node
            node.left = None
    if node.right:
        flatten(node.right, min_node)
    return min_node

set_parents(my_bst)
my_bst.parent = None

root = find_min(my_bst)
pprint(flatten(my_bst, root)) #если не добавить root, то дерево будет разворачиваться только с изначального корня, в данном случае с 7
