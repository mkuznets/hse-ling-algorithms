class Solution(object):
    def moveZeroes(self, nums):
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.append(0)
