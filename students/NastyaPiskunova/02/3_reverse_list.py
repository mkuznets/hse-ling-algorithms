class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
lst.next.next.next.next = lst.next

class Solution:
    def reverseList(self, head):
        tail = ListNode(0)
        while head:
            next = head.next
            head.next = tail.next
            tail.next = head
            head = next
        return tail.next

print(Solution().reverseList(lst))