"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        
        if n!=1 and n%3 !=0:
            return False
        if n == 1 or n==3:
            return True
        
        x = n
        while x!= 1:
            if (x/3) %3 != 0:
                return False
            x /= 3
            x = int(x)
            if x == 3:
                break
                
        return True 
"""
Fast
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0