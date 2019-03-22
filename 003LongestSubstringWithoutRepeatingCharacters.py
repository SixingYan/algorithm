"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
"""
Comments
记录当前字母的位置，如果原来已经出现过，那么就把出现之前的记录全部弹出；如果没有出现过，那就加入字典，同时更新长度

Fast是减少了字典弹出的操作，所以更快
"""
"""
My
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        longest = 1
        begin = 0
        end = 1
        char_to_ix = {s[0]:0}
        while end < len(s):
            if s[end] in char_to_ix.keys():
                pre = char_to_ix[s[end]]
                while begin <=pre:
                    char_to_ix.pop(s[begin], None)
                    begin += 1
                char_to_ix[s[end]] = end
            else:
                char_to_ix[s[end]] = end
                longest = max(longest, len(char_to_ix))
            end += 1
        return longest
            
"""
Fast
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
		maxlen = 0
        currentlen = 0
        indHash = {}
        leftside = -1
        ls = len(s)
        for ind, ch in enumerate(s):
            if (ch in indHash) and (leftside < indHash[ch]):
                leftside = indHash[ch];
            currentlen = ind - leftside;
            if currentlen > maxlen:
                maxlen = currentlen
            indHash[ch] = ind
        currentlen = ls - leftside - 1
        if currentlen > maxlen:
            maxlen = currentlen
        return maxlen