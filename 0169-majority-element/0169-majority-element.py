class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # go through the array using for loop, check if any value appears more than floor(n/2) times in the array, if it does then return the value of that element

        count = {}
        target = len(nums) // 2

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > target:
                return i
               
