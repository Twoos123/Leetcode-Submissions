class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r1, r2 = 0, 0

        # [r1, r2, n, n+1, ......]
        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2




        