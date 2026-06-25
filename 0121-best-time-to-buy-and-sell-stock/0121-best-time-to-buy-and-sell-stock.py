'''understand - 

i - array - prices
o - max(profit)
c - we cant sell before we buy
e - 0 profit 


plan - two pointer 


implement - 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP

