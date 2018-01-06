from hypothesis import given, note
from hypothesis.strategies import integers, lists, randoms, composite, choices
from random import shuffle


@composite
def athlets(draw):
    n = draw(integers(min_value=0, max_value=40))
    ms = lists(integers(min_value=1, max_value=100), min_size=n,
               max_size=n).map(sorted)
    ss = lists(integers(min_value=1, max_value=100), min_size=n, max_size=n,
               unique=True).map(sorted)

    t = list(zip(draw(ms), draw(ss)))
    shuffle(t)

    return t


e = athlets().example()
