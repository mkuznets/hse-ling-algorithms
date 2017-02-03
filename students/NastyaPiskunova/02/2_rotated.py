def findMin(nums):
    a, b = 0, int(len(nums) - 1)
    while a < b:
        c = int((a + b) / 2)
        if nums[c] <= nums[b]:
            b = c
        else:
            a = c + 1
    return nums[a]

print(findMin([4,5,6,7,0,1,2]))