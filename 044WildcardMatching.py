"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
"""
Comments
dp (MY看讨论写出的) greedy (Fast) 很难理解
https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
"""
"""
My
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        # key1 要考虑开头是任意匹配的情况，所以dp的尺寸要多1
        # key2 如果当前模式是*，那么之前的匹配是正确的就可以继续
        # key3 否则就要一对一精确匹配
        # 转移状态 之前的匹配是否成功
        dp = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, 1 + len(p)):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    # 此时到目前为止匹配成功 只能是前一个也是匹配成功
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # p[j-1]对应dp[.][j]
                    # 此时到目前为止匹配成功，可以是
                    # 1. 前s用也是用当前*匹配的，当前还是用*匹配，所以正确与否要看之前匹配是否正确 [i-1][j]，
                    # 2. 前s用前p匹配，当前就用*匹配，所以正确与否要看之前匹配是否正确 [i-1][j-1]
                    # 3. 现在s有前p匹配，当前的*没用上，所以要看之前的匹配是否在正确 [i][j-1]
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 1]
        return dp[-1][-1]
"""
Fast
"""


class Solution:

    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        si = 0
        pi = 0
        save = 0
        star = None
        while si < len(s):
            # 如果此时匹配已经用完
            if pi >= len(p):
                # 然而此时不在*的影响范围内 ❌
                if star is None:
                    return False
                # 重置到*开始位置的下一个地方
                pi = star + 1
                # 前一个s使用*匹配，让s的指针推进
                save += 1
                si = save
                continue

            # 如果文本和匹配正好对应，就同时向前移动一位
            if p[pi] == s[si] or p[pi] == '?':
                pi += 1
                si += 1
                continue

            # 如果此时匹配显示为*
            if p[pi] == '*':
                star = pi
                save = si
                pi += 1
                continue
            #
            if star is not None:
                pi = star + 1
                save += 1
                si = save
                continue

            return False

        for i in range(pi, len(p)):
            if p[i] != '*':
                return False
        return True
