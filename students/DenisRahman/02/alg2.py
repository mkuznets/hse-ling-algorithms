class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z = int(len(nums) - 1)
        x, y = 0, z
        while x < y:
            z1 = (x + y) / 2
            z = int(z1)
            if nums[z] <= nums[y]:
                y = z
            else:
                x = z + 1
        return nums[x]

a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))