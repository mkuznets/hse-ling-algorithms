class Stack(object):
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        return self.stack.pop() if self.stack else None


    def peek(self):
        return self.stack[-1] if self.stack else None


    def isEmpty(self):
        return (self.stack == [])




class MyQueue(object):
    def __init__(self):
        self.stack = Stack()


    def push(self, x):
        self.stack.push(x)


    def pop(self):
        temp_stack = Stack()

        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())

        item = temp_stack.pop()

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

        return item


    def peek(self):
        temp_stack = Stack()

        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())

        item = temp_stack.peek()

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

        return item


    def empty(self):
        return self.stack.isEmpty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()