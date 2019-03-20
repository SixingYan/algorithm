"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

"""
"""
Comments
	走到边缘的时候，就只有一条路能到达出发点
	遍历，计算当前点回到出发点的路径数量
	最后返回终点的路径数量

	和Fast 的思路相同
dp array
"""
"""
My
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 2 and m < 2:
            return 1
        mat = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    mat[i][j] = 1
                elif j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i-1][j]+mat[i][j-1]
        
        return mat[m-1][n-1]
"""
Fast
"""
class Solution:
    def uniquePaths(self, m: 'col', n: 'row') -> 'int':
        
        # edge cases
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        # build the board
        board = [[1 for _ in range(m)] for _ in range(n)]
        
        # DP
        for row in range(1,n):
            for col in range(1,m):
                board[row][col] = board[row-1][col] + board[row][col-1]
        return board[-1][-1]