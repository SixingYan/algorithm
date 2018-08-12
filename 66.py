"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
            num = ''.join([str(p) for p in nums])
        return [int(p) for p in str(int(num) + 1)]
"""
Fast
"""
class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            digits[0] += 1
            return digits
        l = len(digits)
        old = 1
        for i in range(-1, -l - 1, -1):
            remain = (old + digits[i]) % 10
            old = (old + digits[i]) // 10
            digits[i] = remain
        if old == 0:
            return digits
        else:
            return [1] + digits
