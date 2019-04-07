"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
"""
Comments
这个问题可以同时由DP或者Greedy来解决
"""
"""
My
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        转移方程式
        i到达终点最小的步数(nums[i] = k)
        f(i) = 1 + min(f(i+1),f(i+2)...,f(k))
        在寻找[i,k)里找最小值，用线段树找到(这是可以优化的点)
        '''
        n = len(nums)
        dp = [n for _ in range(n)]
        dp[0] = 0
        cur = 0
        for i in range(n):
            left = min(i+nums[i],n)
            j = cur+1
            while j < n and j <= i+nums[i]:
                # dp[j] 到达j最小需要的步数
                dp[j] = min(dp[j],dp[i]+1)
                j += 1
            cur = max(cur, i+nums[i])
        return dp[-1]
        '''
        也可以理解为 左右两个指针，
        下一个左指针是原来右指针的位置，
        下一个右指针是原来左右指针之间的位置+跳跃距离中最大的那个距离。
        这个解法相当于贪心算法
        '''
        if len(nums) <= 1:
            return 0
        left, right = 0, nums[0]
        times = 1
        while right < len(nums) - 1:
            times += 1
            nxt = max(i+nums[i] for i in range(left, right+1))
            left, right = right, nxt
        return times
        
"""
Fast
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        max_reach = [i+v for i,v in enumerate(nums)]
        max_of_left = [0]
        for i in range(n):
            max_of_left.append(min(n-1, max(max_reach[i], max_of_left[-1])))
        cnt = 0
        i = n-1
        while i > 0:
            cur = i
            while max_of_left[i-1] >= cur:
                i -= 1
            i -= 1
            cnt += 1
        return cnt