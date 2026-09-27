class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        majority = len(nums) // 2

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
            if count[i] > majority:
                return i
    
