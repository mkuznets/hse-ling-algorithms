from collections import Counter
from heapq import heapify, heappop, heappush

from .common import Node, encoding_table


def huffman_encode(text, arity):
    """
    Кодирует строку текста алгоритмом Хаффмана с заданным
    количеством символов выходного алфавита

    :param text: текст для кодирования
    :param arity: количество символов выходного алфавита (от 2 до 16)
    :return: tuple: (<дерево декодирования>, <закодированная строка>)

    >>> huffman_encode('helloworld', 2)
    >>> '000101111110110001001111010'

    >>> huffman_encode('abcdefghijklmnop', 16)
    >>> '0123456789abcdef'
    """

    assert 2 <= arity <= 16

    f = [Node(l, freq=f) for l, f in Counter(text).items()]
    heapify(f)

    while len(f) != 1:
        top = [heappop(f) for _ in range(min(len(f), arity))]

        freq = sum(t.freq for t in top)

        z = Node(
            None,
            freq=freq,
            children=top
        )

        heappush(f, z)

    tree = f.pop()
    mapping = encoding_table(tree)

    return (tree, ''.join([mapping[c] for c in text]))
