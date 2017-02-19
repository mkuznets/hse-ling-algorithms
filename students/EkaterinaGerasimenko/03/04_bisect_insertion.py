from bisect import *

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        index = bisect(A,key,hi=j)
        for i in range(j,index,-1):
            A[i] = A[i-1]
        A[index] = key
    return A
