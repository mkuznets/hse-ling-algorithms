from bisect import bisect_right

def insertion_sort(A):
    for j in range(0, len(A)-1):
        key = A[j]
        index = bisect_right(A, key, hi = j)
        for i in range(j, index, -1):
            A[i] = A[i-1]
        A[index] = key

    return A


ary = [54,1,2,3,52,3,1,2,3,5,3,67,3,2,543]
print (insertion_sort(ary))
