"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

https://leetcode.com/problems/valid-sudoku/

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
"""
Comments

Fast 的做法 是直接把三个表合一了，用tuple的方式来存储
"""
"""
My
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 分别建三个集合来做“存在性”验证
        # 行 列 正方区域
        row = [set([]) for _ in range(9)]
        col = [set([]) for _ in range(9)]
        area = [set([]) for _ in range(9)]
        res = True
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue
                    
                if v in row[i]:
                    return False
                else:
                    row[i].add(v)
                    
                if v in col[j]:
                    return False
                else:
                    col[j].add(v)
                    
                idx = (i//3)*3 + j//3
                if v in area[idx]:
                    return False
                else:
                    area[idx].add(v)

        return res
"""
Fast
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()
        for i in xrange(0,9):
            for j in xrange(0,9):
                if board[i][j] != ".":
                    curr = board[i][j]
                    if (i,curr) in big or (curr,j) in big or (i/3,j/3,curr) in big:
                        return False
                    big.add((i,curr))
                    big.add((curr,j))
                    big.add((i/3,j/3,curr))
        return True