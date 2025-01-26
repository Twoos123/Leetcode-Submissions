class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in dic:
                return [dic[comp], i]
            else:
                dic[n] = i
        