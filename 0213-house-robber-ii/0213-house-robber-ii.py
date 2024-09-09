class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        r1, r2 = 0, 0

        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2
        

        