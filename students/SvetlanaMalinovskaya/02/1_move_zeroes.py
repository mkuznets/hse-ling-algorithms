class Solution(object):
    def moveZeroes(self, nums):
        zeroes = 0
        element = 0

        for index in range(len(nums)):
            if nums[index] == 0:
                zeroes += 1
            else:
                nums[element] = nums[index]
                element += 1

        for index in range(len(nums)-1, len(nums)-zeroes-1, -1):
            nums[index] = 0