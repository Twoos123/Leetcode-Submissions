class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        else:
            l, r = 0, len(height) - 1
            res = 0
            maxLeft, maxRight = height[l], height[r]
            while l < r:
                if maxLeft < maxRight:
                    l += 1
                    maxLeft = max(maxLeft, height[l])
                    res += maxLeft - height[l]
                elif maxLeft >= maxRight:
                    r -= 1
                    maxRight = max(maxRight, height[r])
                    res += maxRight - height[r]
            return res



