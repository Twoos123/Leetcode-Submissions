class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0

        for i in nums:
            if i != val:
                nums[k] = i
                k += 1

        return k
            
        

        