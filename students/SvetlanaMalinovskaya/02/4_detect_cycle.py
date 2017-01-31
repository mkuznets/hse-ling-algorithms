# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def hasCycle(self, head):
        # Сложность O(n)
        nodesSeen = {}

        node = head
        while node:
            if node in nodesSeen:
                return True

            nodesSeen[node] = True
            node = node.next

        return False