class Solution(object):
    def moveZeroes(self, nums):
        zeroes = []
        length = len(nums)

        for index in range(length):
            if nums[index] == 0:
                zeroes.append(index)

        last = length-1
        while zeroes:
            index = zeroes.pop()
            nums[index], nums[last] = nums[last], nums[index]
            last -= 1