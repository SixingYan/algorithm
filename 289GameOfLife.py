"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 3 -> 1 live
        # -1 -> 1 die
        # 2 -> 0 to live
        # -2 -> 0 die
        d = {3:1, -1:1, 1:1, 2:0, -2:0, 0:0}
        rd = {3:1, -1:0, 2:1, -2:0}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                die = 0
                if i-1 > -1:
                    if d[board[i-1][j]] == 0:
                        die += 1
                    else:
                        live += 1
                if i-1 > -1 and j-1>-1:
                    if d[board[i-1][j-1]] == 0:
                        die += 1
                    else:
                        live += 1
                if j-1>-1:
                    if d[board[i][j-1]] == 0:
                        die += 1
                    else:
                        live += 1
                if i+1 < m:
                    if d[board[i+1][j]] == 0:
                        die += 1
                    else:
                        live += 1
                if j+1 < n:
                    if d[board[i][j+1]] == 0:
                        die += 1
                    else:
                        live += 1
                if i+1 <m and j+1 < n:
                    if d[board[i+1][j+1]] == 0:
                        die += 1
                    else:
                        live += 1
                if i+1 < m and j-1>-1:
                    if d[board[i+1][j-1]] == 0:
                        die += 1
                    else:
                        live += 1
                if i-1 > -1 and j+1<n:
                    if d[board[i-1][j+1]] == 0:
                        die += 1
                    else:
                        live += 1
                    
                if board[i][j] == 1:
                    if live < 2:
                        board[i][j] = -1
                    elif live == 2 or live == 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = -1
                else:
                    if live == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = -2
                        
        for i in range(m):
            for j in range(n):
                board[i][j] = rd[board[i][j]]
"""
Fast
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        d = {} # {indices : [neighbors]}
        for i in range(len(board)): # rows
            for j in range(len(board[0])):
                d[(i,j)] = []
                if i > 0:
                    d[(i,j)].append(board[i-1][j]) # left
                if j > 0:
                    d[(i,j)].append(board[i][j-1]) # down
                if i>0 and j>0: 
                    d[(i,j)].append(board[i-1][j-1]) # diagonal
                if i<len(board)-1:
                    d[(i,j)].append(board[i+1][j]) # right
                if j<len(board[0])-1:
                    d[(i,j)].append(board[i][j+1]) # up
                if i<len(board)-1 and j<len(board[0])-1:
                    d[(i,j)].append(board[i+1][j+1]) # diagonal
                if i>0 and j<len(board[0])-1:
                    d[(i,j)].append(board[i-1][j+1])
                if i<len(board)-1 and j>0:
                    d[(i,j)].append(board[i+1][j-1])
        
        for k,v in d.items():
            state = sum(v)
            if state < 2 and board[k[0]][k[1]] == 1:
                board[k[0]][k[1]] = 0
            if state > 3 and board[k[0]][k[1]] == 1:
                board[k[0]][k[1]] = 0
            if (state == 2 or state == 3) and board[k[0]][k[1]] == 1:
                board[k[0]][k[1]] = 1
            if state == 3 and board[k[0]][k[1]] == 0:
                board[k[0]][k[1]] = 1