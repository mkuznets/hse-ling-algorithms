class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        self.parent = None

def find_max(self, node):
    if node is None:
        return
    if node.right:
        find_max(node.right)
    elif node.right is None:
        return node
    
def find_min(self, node):
    if node is None:
        return
    if node.left:
        find_min(node.left)
    elif node.left is None:
        return node
            
def set_parents(self, node):
    if node is None:
        return
    if node.left:
        node.left.parent = node
        set_parents(node.left)
    if node.right:
        node.right.parent = node
        set_parents(node.right)

# первым node считаем root
#и считаем, что set_parents() уже была применена

def flatten(self, node):
    if node is None:
        return
    par = node.parent
    if node.left:
        if node.left.right:
            m_node = find_max(node.left)
            m_node.right = node
            par.right = m_node 
        elif node.left.right is None:
            node.left.right = node
            par.right = node.left.right
            flatten(node.left)
    elif node.left is None:
        if node.right.left:
            m_node = find_min(node.right)
            m_node.right = node.right
            m_node.parent = node
        elif node.right.left is None:
            flatten(node.right)
    return node
            
