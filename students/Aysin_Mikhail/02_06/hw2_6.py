#coding: utf-8

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # положить элемент в стек
        self.items.append(item)

    def pop(self):  # удалить элемент из стека и вернуть его значение
        return self.items.pop()

    def peek(self):  # вернуть значение последнего элемента стека (не удаляя его)
        return self.items[-1]

    def isEmpty(self):  # вернуть True, если стек пуст, иначе вернуть False
        return self.items == []


class MyQueue:
    # метод для перезаписи стека для выдачи
    def _fill_pop_stack(self):
        while not self.stack_push.isEmpty():
            self.stack_pop.push(self.stack_push.pop())

    def __init__(self):
        #В этот стек будем записывать
        self.stack_push = Stack()
        #Из этого стека будем доставать
        self.stack_pop = Stack()

    def enqueue(self, item):  # положить элемент в очередь
        self.stack_push.push(item)

    def dequeue(self):  # удалить элемент из очереди и вернуть его значение
        # Если стэк из которого достаем - пустой
        if self.stack_pop.isEmpty():
            # Переписываем в него элементы из стэка для записи
            self._fill_pop_stack()
        # Теперь просто достаем элемент из стека для выдачи
        return self.stack_pop.pop()

    def peek(self):  # вернуть значение первого элемента очереди (не удаляя его)
        # Если стэк из которого достаем - пустой
        if self.stack_pop.isEmpty():
            # Переписываем в него элементы из стэка для записи
            self._fill_pop_stack()
        # Теперь просто показываем элемент из стека для выдачи
        return self.stack_pop.peek()

    def isEmpty(self):  # вернуть True, если стек пуст, иначе вернуть False
        return self.stack_push.isEmpty() and self.stack_pop.isEmpty()


#проверяем как работает очередь
q = MyQueue()
#она должна быть пустая
print(q.isEmpty())
#пишем 1 элемент
q.enqueue(1)
#теперь не пустая
print(q.isEmpty())
#смотрим этот элемент
print(q.peek())
#достаем этот элемент
print(q.dequeue())
#теперь пустая
print(q.isEmpty())
#теперь несколько элментов несколько раз
[q.enqueue(i) for i in range(10)]
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
#верхний должен быть 4
print(q.peek())
#запишем еще
[q.enqueue(i+100) for i in range(10)]
#выводим все
while not q.isEmpty():
    print(q.dequeue())
#всё ок!
