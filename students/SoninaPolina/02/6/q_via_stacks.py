class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, item): 
        self.stack1.append(item)
        
    def pop(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        item = self.stack2.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())        
        return item
    
    def peek(self):
        return self.stack1[0]
    
    def empty(self): 
        if len(self.stack1) == 0:
            return True
        else:
            return False
