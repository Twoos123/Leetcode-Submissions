class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0

        while l < r:
            if(nums[l] + nums[r] < target):
                res += r - l
                l += 1
            else:
                r -= 1
        return res




        