class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        goalP = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalP:
                goalP = i
        
        return True if goalP == 0 else False




        