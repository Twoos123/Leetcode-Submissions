class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        l = 0
        
        for r in range(len(nums)):
            if l < 2 or nums[r] != nums[l - 2]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return l