"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5s
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or s == '':
            return 0
        words = s.strip()
        if words == '':
            return 0

        word_list = words.split(' ')
        if len(word_list)== 0 :
            return 0
        else:
            return len(word_list[-1])
"""
Fast
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip()
        slist = s.split()
        return len(slist[-1]) if slist!=[] else 0