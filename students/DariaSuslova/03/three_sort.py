def partition(A, pivot, lo):
    hi = len(A)-1
    i = 0
    j = 0
    while j in range (0, hi):
        if A[j] == pivot:
            j+=1
        elif A[j] == lo:
            A[i], A[j] = A[j], A[i]
            i += 1
        else:
            A[hi], A[j] = A[j], A[hi]
            hi -=1

   
   


def three_sort(A):
    partition(A, 'W', 'R')
    return A

print(three_sort(['W', 'W', 'B', 'R', 'B', 'R', 'B', 'W', 'R']))
