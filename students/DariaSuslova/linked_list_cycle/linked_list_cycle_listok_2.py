class Solution(object):
    def hasCycle(self, head):
        i = head
        j = head.next
        while i is not None and i.next is not None:
            if i.next == head:
                return True
            i = i.next
            j.next = head
            j = i
        return False


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))  # 1 -> 2 -> 3 -> 4
lst.next.next.next.next = lst.next  # создаём цикл  1 -> 2 -> 3 -> 4 ↘
c = Solution()                                    #                     ↖__________|
print(c.hasCycle(lst))
