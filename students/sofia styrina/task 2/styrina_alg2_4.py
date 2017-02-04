class ListNode:
    def __init__(self, x, next = None):
        self.value = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
lst.next.next.next.next = lst.next # создаём цикл  1 -> 2 -> 3 -> 4 ↘
                                   #                     ↖__________|
class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

print(Solution().hasCycle(lst))
