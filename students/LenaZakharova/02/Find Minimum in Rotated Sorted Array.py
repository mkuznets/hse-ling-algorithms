class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        middle = int(right / 2)
        while nums[middle] > nums[middle - 1] and left < right:
            if nums[middle + 1] < nums[middle] or nums[middle - 1] > nums[middle]:
                return nums[middle + 1]
            elif nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = int((left + right) / 2)

        return nums[middle]

