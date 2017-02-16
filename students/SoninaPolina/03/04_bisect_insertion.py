from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        k = bisect_left(A, key, hi = j)
        for i in range(j,k,-1):
            A[i] = A[i-1]
        A[k] = key
    return A

print(insertion_sort([0,5,2,3,7,6,9,2,0]))
