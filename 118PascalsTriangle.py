"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        data = []
        now = 0

        while now <= numRows:
            if now == 0:
                now += 1
                continue

            if now == 1:
                data.append([1])        # [[1]]
                now += 1
                continue

            if now == 2:
                data.append([1, 1])     # [[1], [1,1]]
                now += 1
                continue

            if now >= 3:
                tem = [1]
                last = data[now - 1 - 1]
                for i in range(len(last) - 1):
                    tem.append(last[i] + last[i + 1])
                tem.append(1)
                data.append(tem)
            now += 1

        return data
"""
Fast
"""
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1] * n for n in xrange(1, numRows + 1)]
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
