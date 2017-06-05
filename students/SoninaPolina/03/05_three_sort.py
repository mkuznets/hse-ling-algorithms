def partition(A, lo, hi, L):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] != L:
            A[i], A[j] = A[j], A[i]
            i += 1            
    A[i], A[hi] = A[hi], A[i]
    return i

def three_sort(A):
    pivot = partition(A, 0, len(A)-1, 'B')
    partition(A, 0, pivot-1, 'W')
    return A

print(three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W', 'B', 'R', 'W', 'W', 'B', 'R', 'R']))
