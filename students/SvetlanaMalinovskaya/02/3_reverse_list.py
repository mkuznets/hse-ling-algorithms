# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        node = head
        tail = None

        while node:
            next = node.next
            node.next = tail
            tail = node
            node = next

        return tail