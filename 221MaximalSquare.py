"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
"""
Comments
Fast is the same
关键点是从1开始，只关注左上角三个点的取值
如果本身就是0，就直接跳过

这个和 找最大矩形 的问题可以进行比较

dp 
"""
"""
My
"""


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        nums = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        # 这一步只是初始化area，选择的是横0列和竖0列中最大的数作为初始area数值（0或者1）
        area = max(max(nums[0]), max(n[0] for n in nums))

        for i in range(1, m):
            for j in range(1, n):
                if nums[i][j] == 1:
                    nums[i][j] = 1 + min(nums[i - 1][j - 1],
                                         nums[i - 1][j], nums[i][j - 1])
                    area = max(area, nums[i][j])
        return area ** 2
"""
Fast
"""
