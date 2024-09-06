from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define code logic
        # loop through prices
        # check next day price
        # higher than current?
        # buy on current day

        # points:
        # you can buy and sell at the same day (consider)
        # you can only hold one share at a time
        # you are given the entire array of prices, ie. access to all days and all prices

        maxProfit = 0

        for i in range(0, len(prices)-1):
            currVal = prices[i]
            nextVal = prices[i+1]

            if nextVal > currVal:
                maxProfit += nextVal - currVal

        return maxProfit
    


prices = [7,1,5,3,6,4]
sol = Solution()
maxProfit = sol.maxProfit(prices)
print(f'max profit: {maxProfit}')
