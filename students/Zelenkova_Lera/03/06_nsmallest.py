def partition(A, lo, hi):
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i





def nsmallest(m, A, lo, hi):  #вызываем от lo=0, hi = len(A)-1
    z = partition(A, lo=lo, hi=hi)
    if m < z+1:
        lo=0
        hi = z-1
        nsmallest(m, A, lo, hi)
    elif m > z+1:
        lo=z+1
        hi=len(A)-1
        nsmallest(m, A, lo, hi)
    elif m == z+1:
        return A[:m]
    return A[:m]


#print(nsmallest(7, [44, 64, 21, 86, 40, 46, 95], 0, 6))
