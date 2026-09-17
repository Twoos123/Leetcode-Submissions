class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # have a left pointer and right pointer start at 0, move the right pointer incrementally through the length of the array, if r lands on a non zero number, swap it with the left pointer and then increment the left pointer by 1.

        l = 0 # start left pointer at 0

        for r in range(len(nums)): # start right pointer at 0 and then traverse the array one by one, right pointer is a scout
            if nums[r] != 0: # if right pointer spots a number that isnt a zero
                nums[l], nums[r] = nums[r], nums[l] # swap the places of the left pointer values and right pointer values, we would be swapping a 0 for a non 0 number everytime
                l += 1 # increment the left pointer by one so eventually itll reach the end of the list and all 0s end up at the end end of the list
