"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
"""
Comments
	dp string
"""
"""
My
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = []
        for i in range(len(s)):
            if i>0 and s[i-1] == s[i]:
                c = 0
                while i-c-1 > -1 and i+c < len(s):
                    if s[i-c-1] != s[i+c]:
                        break
                    c += 1
                count.append(s[i-1-c+1:i+c])
            if i>1 and s[i-2] == s[i]:
                c = 0
                while i-c-2 > -1 and i+c < len(s):
                    if s[i-c-2] != s[i+c]:
                        break
                    c += 1
                count.append(s[i-2-c+1:i+c])
        if len(count) == 0:
            if len(s) > 0:
                return s[0]
            else:
                return ''
        elif len(count) == 1:
            return count[0]
        else:
            l = [len(p) for p in count]
            return count[l.index(max(l))]
"""
Fast
"""
class Solution:
    head = 0
    max_length = 0
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        for idx in range(len(s) - 1):
            self.search_palindrome(s, idx, idx)
            self.search_palindrome(s, idx, idx + 1)
        return s[self.head:self.head + self.max_length]
            
    def search_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.max_length < right - left - 1:
            self.head = left + 1
            self.max_length = right - left - 1