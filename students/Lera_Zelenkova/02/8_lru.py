class LRUCache(object):
    def __init__(self, capacity):
        self.diction = dict()
        head = Node('head', 'head')
        tail = Node('tail', 'tail', prev=head)
        head.next = tail
        self.linklist = LinkedList(head, tail)
        self.capacity = capacity

    def get(self, key):
        if key in self.diction:
            node = self.diction[key]
            self.linklist.remove(node)
            self.linklist.insert_after_head(node)
            return self.diction[key].value
        return -1

    def put(self, key, value):
        if key in self.diction:
            node = self.diction[key]
            node.value = value
            self.linklist.remove(node)
            self.linklist.insert_after_head(node)

        else:
            if len(self.diction) < self.capacity:
                self.diction[key] = Node(key, value)
                self.linklist.insert_after_head(self.diction[key])

            else:
                last_node = self.linklist.tail.prev
                self.linklist.remove(last_node)
                del (self.diction[last_node.key])
                self.diction[key] = Node(key, value)
                self.linklist.insert_after_head(self.diction[key])


class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.key = key


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head  # fst elem
        self.tail = tail  # lst elem

    def insert_after_head(self, node):  # между head и вторым эл-м
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
