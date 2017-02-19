class Solution(object):
    def findMin(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                j = i
        return nums[j]
