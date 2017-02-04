class Solution(object):
    def reverseList(self, head):
        last = None
        current = head
        while(current is not None):
            nxt = current.next
            current.next = last 
            last = current
            current = nxt
        return last
