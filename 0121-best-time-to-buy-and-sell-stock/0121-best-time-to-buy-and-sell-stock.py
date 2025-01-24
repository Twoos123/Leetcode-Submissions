class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = buy, right = sell
        maxProfit = 0

        while r < len(prices): #while price to sell is less than the length of prices
            if prices[l] < prices[r]: #while there is potential to make profit, (buy and then sell)
                profit = prices[r] - prices[l] #calculate profit
                maxProfit = max(maxProfit, profit) #take max of profit and maxprofit
            else:
                l = r #if no profit can be made, make left and right go to the same place to go to minimum
            r += 1 #update right pointer till the end of the list
        return maxProfit #return maxprofit

       