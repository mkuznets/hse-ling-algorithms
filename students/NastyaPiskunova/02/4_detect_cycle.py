class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
lst.next.next.next.next = lst.next

class Solution:
    def hasCycle(self, head):
        low = high = head
        while high and high.next:
            low = low.next
            high = high.next.next
            if low == high:
                return True
        return False

print(Solution().hasCycle(lst))

