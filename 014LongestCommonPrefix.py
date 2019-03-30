"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if min(len(w) for w in strs) == 0:
            return ""
        if len(set([w[0] for w in strs]))==0:
            return ""
        l = sorted(strs, key=lambda s: len(s))
        p = l[0]
        for i in range(len(l)-1, 0, -1):
            n = 0
            for j,c in enumerate(p):
                if p[j] == l[i][j]:
                    n += 1
                else:
                    break
            if n == 0:
                p = ""
                break
            else:
                p=p[:n]
        return p
"""
Fast
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        r = strs[0]
        length = len(r)
        for a in strs:
            tag = 0
            while(tag == 0):
                if r[0:length] == a[0:length]:
                    tag = 1
                else:
                    length = length - 1
        return r[0:length]