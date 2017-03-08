class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))  # 1 -> 2 -> 3 -> 4
lst.next.next.next.next = lst.next  # создаём цикл  1 -> 2 -> 3 -> 4 ↘
                                    #                     ↖__________|
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    cur = cur2 = head
    while cur2 and cur2.next:
        cur = cur.next
        cur2 = cur2.next.next
        if cur == cur2:
            return True
    return False

print(hasCycle(lst))
