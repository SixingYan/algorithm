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
这题是hard 阿里有出过，很难理解。

My 参考了 动态规划的解法
求两次交易的最大收益，转化为在原数组中求两段最大子序列的问题，
找到 0~i 最大差值的子序列，
找到 i~n 最大差值的子序列

然后看同一个i时刻，两者之和最大，就是选择卖出买入的时刻，
两者之和就是收益最大的值


Fast的解法比较巧妙

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


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp1 = [0] * n  # 0~i 最大收益
        dp2 = [0] * n  # n~i 最大收益

        # 从左到右找最小
        minp = prices[0]
        for i in range(1, n):
            # 找到最小
            minp = min(minp, prices[i])
            # 更新截止到当前的最大收益(算之前的收益（不买卖），还是卖出)
            dp1[i] = max(dp1[i - 1], prices[i] - minp)

        # 从右到左找最大（从后往前遍历）
        maxp = prices[-1]
        for i in range(n - 2, -1, -1):
            maxp = max(maxp, prices[i])
            # 从卖出看什么时候买入，因为卖出不超过最后一天
            dp2[i] = max(dp2[i + 1], maxp - prices[i])
        # 看哪一个时刻收益高
        return max(dp1[i] + dp2[i] for i in range(n))

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
