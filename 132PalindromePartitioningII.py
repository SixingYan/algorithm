"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
"""
Comments
"""
"""
My
"""


class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [_ for _ in range(n)]
        # p[start][end] [j][i] 表示从start~end的位置是不是回文
        p = [[False] * n for _ in range(n)]
        p[0][0] = True

        # i 是 end, j 是 start
        for i in range(1, n):
            for j in range(i, -1, -1):

                if s[i] == s[j]:
                    # i-j<2 说明长度为1，肯定是回文
                    # j+1~i-1 是它的子串
                    if i - j < 2 or p[j + 1][i - 1] is True:
                        # j=0时 表示当前从0~i，此时如果是回文，则最小分割次数应该为0
                        # 不然就是 从它的子串的最小分割次数+1，表示当前i处切一刀，i之前的是回文
                        dp[i] = min(dp[i], 0 if j == 0 else dp[j - 1] + 1)
                        p[j][i] = True

        return dp[-1]
"""
Fast
"""


class Solution(object):

    def minCut(self, s):
        # 这里会有一个直接检查的操作
        # acceleration
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        # algorithm
        # cut numbers in worst case (no palindrome)
        cut = [x for x in range(-1, len(s))]

        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome
            # exists

            # 以每一个位置为中心，查找可能的最长的回文位置

            # odd palindrome
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1

            # even palindrome
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                # 这里位置每次增2
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1

        return cut[-1]
