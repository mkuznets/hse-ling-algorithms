# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        if current is None:
            return False
        else:
            current2 = head.next
            while current != current2:
                if current is None or current2 is None or current2.next is None or current2.next.next is None:
                    return False
                else:
                    current = current.next
                    current2 = current2.next.next
            return True
