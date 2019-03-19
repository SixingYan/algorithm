"""
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
"""
"""
Comments
这是最直接的思路。从第二天开始考虑sell，如果buy-sell为负数，说明当前是一个比buy更低的价格，应该替换buy的价格
一直更替maxprofit的值

Greedy Array
"""
"""
My
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        sell = 1
        buy = 0
        mp = 0
        while sell < len(prices):
            p = prices[sell] - prices[buy]
            mp = max(mp, p)
            # this means, there is a day when the stock price is less than that
            # of current stock buying date, hence buy stock that day
            if p < 0:
                buy = sell
            sell += 1
        return mp
"""
Fast
"""
