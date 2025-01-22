class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set(nums)

        for i in nums:
            if nums.count(i) == 1:
                return i
        
        #more efficient
        # result = 0
        #for num in nums:
        #    result ^= num  # XOR all numbers
        #return result
