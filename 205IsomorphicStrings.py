"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.analysis(list(s)) == self.analysis(list(t))
        
    def analysis(self, s):
        arr = []
        d = {}
        idx = 0
        for i in range(len(s)):
            if s[i] in d.keys():
                arr.append(d[s[i]])
            else:
                d[s[i]] = idx
                arr.append(idx)
                idx += 1

        return arr
"""
Fast
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        length = len(s)
        dict_values = {}
        for i in range(length):
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dict_values:
                    if s[i] != dict_values[t[i]]:
                        return False
                s_to_t[s[i]] = t[i]
                dict_values[t[i]] = s[i]
        return True