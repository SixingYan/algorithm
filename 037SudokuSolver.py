"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...

https://leetcode.com/problems/sudoku-solver/

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
"""
Comments

直接的方法是使用 DFS, 直接每种填充方法往下尝试。注意如果尝试不成功，需要重置

"""
"""
My
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(cells, rows, cols, area):
            if not cells: # 当已经填完了
                return True
            i, j = cells[-1]
            for v in range(0, 9):
                # 尝试每一个数
                idx = (i//3) * 3 + j // 3
                if rows[i][v] == cols[j][v] == area[idx][v] == 0: # 当前这个数可以尝试
                    rows[i][v] = cols[j][v] = area[idx][v] = 1
                    board[i][j] = str(v + 1)
                    if dfs(cells[:-1], rows, cols, area):
                        return True

                    # 如果上一步没有return，说明当前n这个数不行，重置
                    board[i][j] = '.'
                    rows[i][v] = cols[j][v] = area[idx][v] = 0
            return False # 如果没有直接return，就说明默认情况下不成功
        
        rows = [[0]*9 for _ in range(9)]
        cols = [[0]*9 for _ in range(9)]
        area = [[0]*9 for _ in range(9)]
        cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    cells.append((i,j))
                else:
                    v = int(board[i][j])-1
                    idx = (i//3) * 3 + j // 3
                    rows[i][v] = cols[j][v] = area[idx][v] = 1
        dfs(cells, rows, cols, area)
"""
Fast
"""
