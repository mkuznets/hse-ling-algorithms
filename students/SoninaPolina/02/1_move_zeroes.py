class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
