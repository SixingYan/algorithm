"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
"""
Comments
这题是hard 阿里有出过，很难理解。My 参考了 Fast的解法

这里只允许两次交易，依次考虑:
1. 如果当前是第二支股票卖出
2. 如果当前是第二支股票买入
3. 如果当前是第一支股票卖出
4. 如果当前是第一支股票买入
array dp
"""
"""
My
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        hd1 = hd2 = float("-inf")  # 第一次买，第二次买
        re1 = re2 = 0  # 第一次卖，第二次卖
        for p in prices:
            re2 = max(re2, hd2 + p)
            hd2 = max(hd2, re1 - p)
            re1 = max(re1, hd1 + p)
            hd1 = max(hd1, -p)
        return re2
"""
Fast
"""
The thinking is simple and is inspired by the best solution from Single Number II(I read through the discussion after I use DP).
Assume we only have 0 money at first
4 Variables to maintain some interested 'ceilings' so far:
The maximum of if we've just buy 1st stock, if we've just sold 1nd stock, if we've just buy 2nd stock, if we've just sold 2nd stock.
Very simple code too and work well. I have to say the logic is simple than those in Single Number II.

public class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE
        int release1 = 0, release2 = 0
        for(int i: prices){ // Assume we only have 0 money at first
                           release2 = Math.max(release2, hold2+i)
                           // The maximum if we've just sold 2nd stock so far.
                           hold2 = Math.max(hold2,    release1 - i)
                            // The maximum if we've just buy  2nd stock so far.
                           release1 = Math.max(release1, hold1 + i)
                            // The maximum if we've just sold 1nd stock so far.
                           hold1 = Math.max(hold1,    -i)
                            // The maximum if we've just buy  1st stock so far.
                           }
        return release2
        // /Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}