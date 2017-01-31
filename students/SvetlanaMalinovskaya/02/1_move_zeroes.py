class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        last = length-1

        for index in range(last, 0, -1):
            if nums[index] == 0:
                nums[index], nums[last] = nums[last], nums[index]
                last -= 1