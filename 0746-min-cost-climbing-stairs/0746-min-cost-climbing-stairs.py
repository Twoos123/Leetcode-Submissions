class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        n = len(cost)
        dp = [float('inf')] * (n + 1)
        
        dp[0] = 0 # if index 0 then no money spent
        dp[1] = 0 # if index 1 then no money spent

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]