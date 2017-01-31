class HashTable(object):
    def __init__(self):
        self.filled = 0
        self.size = 1000
        self.table = [None for _ in range(self.size)]


    def _get_hash(self, element):
        # Как-бы приватный метод для расчёта хэша
        return hash(element) % self.size


    def add(self, element):
        # Возвращает -1, если таблица заполнена
        # Иначе просто добавляет значение в таблицу
        if self.filled == self.size:
            return -1

        if self.find(element):
            return

        key = self._get_hash(element)

        if self.table[key] is not None:
            while self.table[key] is not None:
                key += 1

        self.table[key] = element
        self.filled += 1


    def remove(self, element):
        # Удаляет заданный элемент из таблицы
        key = self._get_hash(element)

        # Удалять только если элемент есть в таблице
        if self.find(element):
            if key < self.size-1:
                while self.table[key] == self.table[key+1]:
                    key += 1

            self.table[key] = None
            self.filled -= 1


    def find(self, element):
        return (self.table[self._get_hash(element)] is not None)