def moveZeroes(nums):
    y = 0
    for x in range(len(nums)):
        if nums[x]:
            nums[x], nums[y] = nums[y], nums[x]
            y += 1
    return nums

print(moveZeroes([0,1,0,3,12]))