nums = [4, 5, 6, 7, 0, 1, 2]
class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = int(l + (r - l) / 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

print(Solution().findMin(nums))
