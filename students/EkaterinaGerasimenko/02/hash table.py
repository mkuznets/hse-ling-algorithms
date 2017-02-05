class HashTable:
    def __init__(self):
        self.table = [None]*1000

    def __repr__(self):
        return str(self.table)

    def add(self, element):
        # добавить элемент в хэш-таблицу или сообщить, что мест нет
        position = hash(element) % 1000
        initposition = position
        occupied = True
        while occupied and position != initposition - 1:
            if self.table[position] is None:
                self.table[position] = element
                occupied = False
            position += 1
            if position == len(self.table):
                if initposition == 0:
                    position = -1
                else:
                    position = 0
        if occupied and self.table[position] is None:
            self.table[position] = element
            occupied = False
        if occupied:
            print('no cells available')

    def find(self, element):
        # вернуть True, если элемент есть в хэш-таблице, и False, если нет
        position = hash(element) % 1000
        initposition = position
        while position != initposition - 1:
            if self.table[position] == element:
                return True
            position += 1
            if position == len(self.table):
                position = 0
        return self.table[position] == element
