# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def hasCycle(self, head):
        current_node = head
        next_node = None
        previous_node = None

        if not current_node.next:
            return False

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return (previous_node == head)