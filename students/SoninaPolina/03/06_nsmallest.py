def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

def nsmallest(m, A):
    quicksort(A, 0, len(A)-1)
    return A[:m]

def quicksort(A, start, end):
    if start < end:                       
        pivot = partition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)
        
print(nsmallest(3, [44, 64, 21, 86, 40, 46, 95, 73, 42, 20, 99, 15, 73]))
