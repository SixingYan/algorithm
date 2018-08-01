"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
"""
Comments
"""
"""
My
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            x = self.change(-x)
            if -x < -1 * 2**31:
                res = 0
            else:
                res = -x
        else:
            res = self.change(x)
            if res > 2 ** 31 - 1:
                res = 0
        return res

    def change(self, x):
        nums = list(str(x))
        nums.reverse()

        while nums[0] == '0':
            nums.pop(0)
        return int(''.join(str(p) for p in nums))
"""
Fast
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        bsign = 1
        if x < 0:
            bsign = -1
            x = -x
        res = 0
        maxv = 2 ** 31
        while x != 0:
            res = res * 10 + x % 10
            if res > maxv or (res == maxv and bsign == -1):
                return 0
            x = x / 10
        return bsign * res
