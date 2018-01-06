from string import hexdigits


class Node:
    def __init__(self, letter=None, freq=0, children=None):
        self.letter = letter
        self.freq = freq
        self.children = children or []

    def tuple(self):
        return (self.freq, ord(self.letter) if self.letter else -1)

    def __lt__(self, other):
        return self.tuple() < other.tuple()

    def __eq__(self, other):
        return self.tuple() == other.tuple()


def encoding_table(node, code=''):
    """
    Превращает построенное алгоритмом Хаффмана дерево
    в словарь соответствия символ-код.

    Для кодирования, в зависимости от арности дерева,
    используются символы [0-9abcdef].

    >>> encoding_table(Node(children=[Node('a'), Node('b'), Node('c')]))
    >>> {'a': '0', 'b': '1', 'c': '2'}
    """

    if node.letter is None:
        mapping = {}
        for child, digit in zip(node.children, hexdigits):
            mapping.update(encoding_table(child, code + digit))
        return mapping
    else:
        return {node.letter: code or '0'}
