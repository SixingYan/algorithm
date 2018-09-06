"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:
            return 0
        if x <4:
            return 1
        if len(str(x)) == 1:
            for i in range(int(x*0.25),x):
                v = i ** 2
                if v == x:
                    return i
                elif v > x:
                    return i-1
                else:
                    pass
        else:
            dig_num = int(len(str(x)) / 2)
            dig = int('9' * dig_num)
            while True:
                start = dig ** 2
                if start == x:
                    return dig
                elif start > x:
                    dig = int(dig/2)
                else:
                    if (dig+1) ** 2 > x:
                        return dig
                    else:
                        dig += 1
"""
Fast
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """i = 0
        square = 0
        while square <= x:
            square = i*i
            i += 1
        return i-2
        """
        if x == 1:
            return 1
        l = 0
        r = x
        m = x//2
        while (r-l) > 1:
            if m**2 > x:
                r = m
                m = (r-l)//2
            elif m**2 < x:
                l = m
                m = l+(r-l)//2
            else:
                return m
        return l