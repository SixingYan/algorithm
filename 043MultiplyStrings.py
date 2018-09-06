"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
"""
My
"""


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        elif num1 == '1':
            return num2
        elif num2 == '1':
            return num1
        else:
            pass

        sm, lg = self.prepare(num1, num2)

        result = []
        for i in range(len(sm)):
            n = 0
            base = [0 for _ in range(i)]

            for j in range(len(lg)):

                v = sm[i] * lg[j] + n
                if v > 9:
                    a, b = tuple(list(str(v)))
                    n = int(a)
                    base.append(int(b))
                else:
                    n = 0
                    base.append(v)
            if n != 0:
                base.append(n)

            result.append(base)

        res = []
        n = 0
        for i in range(len(result[-1])):
            v = n + sum(base[i] for base in result if i < len(base))
            if v > 9:
                t = list(str(v))
                n = int(''.join(t[:-1]))
                res.append(t[-1])
            else:
                n = 0
                res.append(v)
        if n != 0:
            res.append(n)
        res.reverse()

        return ''.join(str(p) for p in res)

    def prepare(self, num1, num2):

        a = [int(p) for p in num1]
        b = [int(p) for p in num2]
        a.reverse()
        b.reverse()
        if len(a) > len(b):
            return b, a
        else:
            return a, b

"""
Fast
"""


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int1 = 0
        int2 = 0
        if num1 == "0" or num2 == "0":
            return "0"
        total = ""
        for char in num1:
            int1 *= 10
            int1 += self.getInt(char)
        for char in num2:
            int2 *= 10
            int2 += self.getInt(char)

        numTotal = int1 * int2
        while numTotal != 0:
            digit = numTotal % 10
            numTotal = numTotal / 10
            total = self.getStr(digit) + total

        return total

    def getInt(self, digit):
        mapp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return mapp.get(digit, 0)

    def getStr(self, digit):
        mapp = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        return mapp.get(digit, '0')
