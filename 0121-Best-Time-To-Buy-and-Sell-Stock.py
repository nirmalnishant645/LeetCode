'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price, max_profit = prices[0], 0
        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = price - min_price if price - min_price > max_profit else max_profit
        return max_profit

# Same Approach, Different Solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_profit = 0, 1, 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = profit if profit > max_profit else max_profit
            else:
                buy = sell
            sell += 1
        return max_profit

# Kadane's Algorithm

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            profit = max_profit = 0
            
            for i in range(1, len(prices)):
                profit = max(0, profit + prices[i] - prices[i-1])
                max_profit = max(max_profit, profit)
                
            return max_profit