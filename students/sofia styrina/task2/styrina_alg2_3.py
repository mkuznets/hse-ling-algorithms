class ListNode:
    def __init__(self, x, next = None):
        self.value = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

class Solution:
    def reverseList(self, head):
        head1 = None
        while head:
            x = head
            head = x.next
            x.next = head1
            head1 = x
        return head1

print(Solution().reverseList(lst).value)
