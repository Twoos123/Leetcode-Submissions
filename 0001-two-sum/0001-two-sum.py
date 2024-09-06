class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in dic:
                return [dic[comp], i]
            else:
                dic[num] = i

            
        