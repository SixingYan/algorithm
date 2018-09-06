"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num
        if n <=0:
            return False
        
        if n!=1 and n%4 !=0:
            return False
        if n == 1 or n==4:
            return True
        
        x = n
        while x!= 1:
            if (x/4) %4 != 0:
                return False
            x /= 4
            x = int(x)
            if x == 4:
                break
                
        return True 
"""
Fast
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num>0 and (num==1 or (num%4==0 and self.isPowerOfFour(num/4)))