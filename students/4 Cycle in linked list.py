#Задание 4 (3 балла) цикл в односвязном списке
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    def __str__(self):
        return str(self.val)

def hasCycle(lst, s = set()):
    if lst not in s:
        s.add(lst)
        hasCycle(lst.next)
    else:
        print(True)
    
#node1 = ListNode(1)
#node2 = ListNode(2)
#node3 = ListNode(3)
#node4 = ListNode(4)
#node1.next = node2
#node2.next = node3
#node3.next = node4
#node4.next = node1.next
lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
#print(lst)
lst.next.next.next.next = lst.next
hasCycle(lst)
