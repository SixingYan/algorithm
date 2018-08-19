"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""
"""
Comments
"""
"""
My
"""
class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex
        if k == 0:
            return [1]
        elif k == 1:
            return [1, 1]
        result = [0 for _ in range(k + 1)]
        result[0] = 1
        result[1] = 1

        i = 1
        while i < k:
            # when i=3
            # prior len is 3
            # present len will be 3+1
            result[i + 1] = 1
            for j in range(i, 0, -1):  # not include 0
                result[j] = result[j] + result[j - 1]
            i += 1

        return result
"""
Fast
"""
'I am the fastest!'