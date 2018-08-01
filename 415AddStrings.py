"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
"""
Fast
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ln1=len(num1)
        ln2=len(num2)
        summ=0
        res=""
        carr=0
        while ln1>0 or ln2>0:
            if ln1>0:
                summ+=ord(num1[ln1-1])-ord('0')
                ln1-=1
            if ln2>0:
                summ+=ord(num2[ln2-1])-ord('0')
                ln2-=1
            summ+=carr
            carr=summ//10
            res=str(summ%10)+res
            summ=0
        if carr>0:
            res=str(carr)+res
        return res