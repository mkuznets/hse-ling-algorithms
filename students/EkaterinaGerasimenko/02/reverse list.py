def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        nhead = head.next
        head.next = prev
        prev = head
        head = nhead
    return prev