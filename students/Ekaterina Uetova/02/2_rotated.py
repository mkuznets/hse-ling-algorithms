class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0 
        end = int(len(nums) - 1)
        while start < end:
            middle = int((start + end) / 2)
            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle
        return nums[start]
    