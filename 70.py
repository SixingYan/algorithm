"""
 You are climbing a stair case. It takes n steps to reach to the top.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def climbStairs(self, n): # 我自己的解法，递归，答案正确但是超时了
        """
        :type n: int
        :rtype: int
        """
        return self.step(n)

    def step(self, n):
        if n == 1: # only left 1
            return 1
        elif n == 2: # only left 2
            return 2
        else:
            return self.step(n-1) + self.step(n-2)
    
   def func2(self, n): # 找到有规律的数列
        a = [1,1]
        for i in range(n-1):
            a.append(a[i]+a[i+1])
        return a[-1]
"""
Fast
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0, 1, 2]
        for i in range(3, n+1, 1):
            res.append(res[i-1] + res[i-2])
        return res[n]