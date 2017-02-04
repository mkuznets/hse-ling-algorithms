class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        x = len(nums)
        i = 0
        j = 0
        while i < x:
            print(nums[j])
            print(zeros)
            if nums[j] == 0:
                nums.pop(j)
                zeros += 1
                j -= 1
            j += 1
            i += 1
        for j in range(zeros):
            nums.append(0)