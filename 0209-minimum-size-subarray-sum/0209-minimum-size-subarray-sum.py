class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        l = 0
        res = float('inf')
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                length = r - l + 1
                res = min(res, length)
                window_sum -= nums[l]
                l += 1
    
        return 0 if res == float('inf') else res
