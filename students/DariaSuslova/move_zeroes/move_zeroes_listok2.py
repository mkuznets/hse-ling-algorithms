class Solution(object):
    def moveZeroes(self, nums):
        j=0
        i=0
        while (j<len(nums)):
            if (nums[j] == 0):
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        while (i<len(nums)):
            nums[i] == 0
            i+=1

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


""" Работает немного быстрее, но возвращает нули вначале:(
class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
            while (nums[j] == 0 and j<len(nums)):
                j+=1
                nums[j], nums[i] = nums[i], nums[j]"""
            
