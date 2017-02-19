from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        k = bisect(A, key, 0, j)
        A = A[:k] + [key] + A[k:j] + A[j+1:]

    return A

