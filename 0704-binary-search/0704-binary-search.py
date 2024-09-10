class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
        return -1

        