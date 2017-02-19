from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = bisect(A[:j], key)

        # TODO: Заменить линейный поиск на бинарный.
        # while i>0 and A[i-1]>key:
        #     A[i] = A[i-1]
        #     i -= 1
        # A[i] = key

        A[i + 1:j + 1] = A[i:j]
        i = bisect(A, key, lo=0, hi=j)
        for k in range(j, i):
            A[k] = A[k - 1]
        A[i] = key

    return A

#print(insertion_sort([2, 1, 3, 7, 4, 0, 10]))