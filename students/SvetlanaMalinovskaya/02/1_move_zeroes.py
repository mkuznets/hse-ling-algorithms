class Solution(object):
    def moveZeroes(self, nums):
        temp = []

        while 0 in nums:
            temp.append(nums.pop(nums.index(0)))

        nums += temp