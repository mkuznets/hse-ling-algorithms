import random
import itertools


def gen_case():
    U = {
        random.randint(0, 10)
        for i in range(random.randint(5, 10))
    }
    T = []

    for _ in range(random.randint(1, 10)):
        T.append(set(random.sample(U, random.randint(1, len(U)))))

    R = U - set(list(itertools.chain(*T)))
    if R:
        T.append(R)

    return U, T
