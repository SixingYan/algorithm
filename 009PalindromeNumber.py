"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if -1< x < 10:
            return True

        # cal digs
        ten = 10
        while x/ten >= 1:
            ten *= 10
        ten /= 10
        
        # get dig list
        dig_list = []

        while ten >= 1:
            dig = int(x/ten)
            dig_list.append(dig)

            x -= dig * ten
            ten /= 10
        
        # check list
        for i in range(int(len(dig_list)/2)+1):
            if dig_list[i] != dig_list[len(dig_list)-i-1]:
                return False
        return True
"""
Fast
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or (x % 10 == 0 and x > 0):
            return False
        half = 0
        while x >= half:
            if (x == half) or (x / 10 == half):
                return True
            half = half*10 + x % 10
            x /= 10
        return False