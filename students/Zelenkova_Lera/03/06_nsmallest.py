def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    print(A, i)
    return i





def nsmallest(m, A, lo, hi):  #вызываем от lo=0, hi = len(A)-1
    z = partition(A, lo=lo, hi=hi)
    if m < z:
        lo=0
        hi = z-1
        nsmallest(m, A, lo, hi)
    elif m > z:
        lo=z+1
        hi=len(A)-1
        nsmallest(m, A, lo, hi)
    elif m == z+1:
        return
    return A[:m]
