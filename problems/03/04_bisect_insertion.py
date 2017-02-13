from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j

        # TODO: Заменить линейный поиск на бинарный.
        # while i>0 and A[i-1]>key:
        #     A[i] = A[i-1]
        #     i -= 1
        # A[i] = key

    return A
