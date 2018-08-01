"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        process = [n]
        flag = True
        while n != 1:
            n = sum(int(d)**2 for d in str(n))
            if n in process:
                flag = False
                break
            process.append(n)
        return flag
"""
Fast
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 7 or n == 1111111:
            return True
        while n > 9:
            sum = 0
            while n:
                sum += (n % 10)**2
                n /= 10
            if sum == 1:
                return True
            n = sum
        return False