from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        index = bisect(A[:j],key)
        A[index+1:j+1] = A[index:j]
        A[index] = key
    return A
