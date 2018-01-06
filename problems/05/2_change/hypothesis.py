from hypothesis import given, note
from hypothesis.strategies import integers, lists, randoms, composite, choices
from random import shuffle


@composite
def coins(draw):
    n = draw(integers(min_value=5, max_value=20))
    coins = draw(
        lists(integers(min_value=1, max_value=30), min_size=n, max_size=n).map(
            sorted))
    change = draw(integers(min_value=min(coins) * 2, max_value=200))

    return sorted(set(coins)), change


d = coins().example()
n = grd_change(*d)
print('Input: %s, %d' % d)
print('Expected: %d' % n)
