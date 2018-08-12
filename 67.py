"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
result = []
        sm, lg = self.markSmallBig(a, b)
        n = 0
        i = 0
        j = 0
        while i < len(sm):
            value = sm[i] + lg[i] + n
            if value > 1:
                n = 1
            else:
                n = 0

            v = value % 2
            result.append(v)
            i += 1
            j += 1

        while j < len(lg):
            value = lg[j] + n
            if value > 1:
                n = 1
            else:
                n = 0

            v = value % 2
            result.append(v)
            j += 1
        if n == 1:
            result.append(n)
        result.reverse()

        return ''.join([str(r) for r in result])

    def markSmallBig(self, a, b):
        a = list(a)
        b = list(b)

        a.reverse()
        b.reverse()
        
        a = [int(p) for p in a]
        b = [int(p) for p in b]
        
        if len(a) > len(b):
            return b, a
        else:
            return a, b
"""
Fast
"""
class Solution(object):
    def addBinary(self, a, b):
        return str(bin(int(a,2) + int(b,2)))[2:]