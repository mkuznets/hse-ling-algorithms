class qViaStacks:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) > 0:
            self.stack = self.stack[1:]

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

qvs = qViaStacks()
qvs.push(1)
qvs.push(2)
qvs.push(3)
print(len(qvs.stack))