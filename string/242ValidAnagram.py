"""
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
"""
Comments
数两个词语的字母数量
"""
"""
My
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if self.ia(s) == self.ia(t):
            return True
        else:
            return False
    def ia(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)
"""
Fast
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = 'abcdefghijklmnopqrstuvwxyz'
        for i in l:
            if(s.count(i) != t.count(i)):
                return False
        return True 