"""

"""
"""
Comments two solving way
"""
"""
My
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 2147483648 % n == 0        
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        
        if n!=1 and n%2 !=0:
            return False
        if n == 1 or n==2:
            return True
        
        x = n
        while x!= 1:
            if (x/2) %2 != 0:
                return False
            x /= 2
            x = int(x)
            if x == 2:
                break
                
        return True 
"""
Fast
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        while (num > 1):
            if num % 2 == 1:
                return False
            num /= 2
        if num == 1:
            return True
        return False