class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            else:
                mid = int((start + end)/2)
                if nums[mid] >= nums[start]:
                    start = mid + 1
                elif nums[mid] < nums[start]:
                    end = mid
        return nums[start]