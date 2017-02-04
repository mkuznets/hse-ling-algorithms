nums = [0, 1, 0, 3, 12]
print(nums)

class Solution:
    def moveZeroes(self, nums):
        p = 0
        for x in nums:
            if x!= 0:
                nums[p] = x
                p += 1
        while p < len(nums):
            nums[p] = 0
            p += 1

Solution().moveZeroes(nums)
print(nums)
