from bisect import *


def insertion_sort(A):
    for j in range(1, len(A)):
        # TODO: Заменить линейный поиск на бинарный.
        # while i>0 and A[i-1]>key:
        #     A[i] = A[i-1]
        #     i -= 1
        # A[i] = key
        key = A[j]
        idx = bisect_left(A, key, hi=j)
        i = j - 1
        while i >= idx:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

    return A

# print(insertion_sort([0,5,2,3,7,6,9,2,0]))
# print(insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]))
