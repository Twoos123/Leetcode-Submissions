class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        l = 0
        count = 0
        product = 1
        
        for r in range(len(nums)):

            product *= nums[r]

            while product >= k:
                product = product / nums[l]
                l += 1

            count += (r - l + 1)

        return count


