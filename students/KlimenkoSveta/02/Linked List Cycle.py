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
        if head:
            turtle = head
            if turtle.next:
                hare = turtle.next
                while turtle and hare and hare.next != None:
                    turtle = turtle.next
                    hare = (hare.next).next
                    if turtle == hare:
                        return True
        return False
    
