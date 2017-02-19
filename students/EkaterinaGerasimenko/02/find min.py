def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return rec(len(nums)-1,0,nums)

def rec(hi,lo,arr):
    if arr[lo] < arr[hi]:
        return arr[0]
    if hi == lo:
        return arr[lo]
    mid = (lo + hi) // 2
    if mid > lo and arr[mid] < arr[mid-1]:
        return arr[mid]
    if mid < hi and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    if arr[hi] < arr[mid]:
        return rec(hi,mid,arr)
    return rec(mid,lo,arr)