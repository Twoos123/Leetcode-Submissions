class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        l = 0
        
        for r in range(len(nums)):
            if l == 0 or nums[r] != nums[l - 1]:
                
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return l

        