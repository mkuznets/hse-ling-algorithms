# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def hasCycle(self, head):
        current_node = head
        next_node = None
        previous_node = None

        if current_node.next is None or head is None:
            return False

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return (previous_node == head)


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
head.next = None
a.next = b
b.next = head

print (Solution().hasCycle(head))