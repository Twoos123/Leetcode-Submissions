class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for n in range(len(nums)):
            nums[n] *= nums[n]
        nums.sort()
        return nums


        