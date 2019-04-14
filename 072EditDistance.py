"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
"""
Comments
Hard难度的DP

这里的写法是参照discussion的
参考解释 https://www.cnblogs.com/yulinfeng/p/7096882.html
有一个之前没理解的重要点是，删除一个并不能直接获得目标，只是一种操作而已。

Fast是用递归做的
"""
"""
My
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        #print(dp)
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                # 针对直接完全复制的情况
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                else:
                    dp[i][j] = min(dp[i-1][j]+1, # 对 word1 删除
                         dp[i][j-1]+1, # 对 word1 增加， 相当于word2少了一个
                         dp[i-1][j-1]+(0 if word1[i-1] == word2[j-1] else 1)) # 改变或正好相等
        return dp[-1][-1]
                
                
"""
Fast
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def minDistanceIdx(ia, ib):
            if ia < 0:
                return ib + 1
            elif ib < 0:
                return ia + 1
            if result[ia][ib] == -1:
                if word1[ia] == word2[ib]:
                    result[ia][ib] = minDistanceIdx(ia-1, ib -1)
                else:
                    addDis = minDistanceIdx(ia, ib - 1)
                    delDis = minDistanceIdx(ia-1, ib)
                    repDis = minDistanceIdx(ia - 1, ib - 1)
                    result[ia][ib] = 1 + min(addDis, delDis, repDis)
            
            return result[ia][ib]
        
        result = [[-1]*len(word2) for _ in word1]
        return minDistanceIdx(len(word1)-1, len(word2)-1 )