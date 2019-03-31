"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            if word == "":
                return True
            return False
        n = len(board[0])
        if n == 0:
            if word == "":
                return True
            return False
        flag = False
        def check(x,y,idx):
            if (x,y) in stack:
                return False
            if x<0 or x > m-1 or y < 0 or y > n-1:
                return False
            if board[x][y] != word[idx]:
                return False
            if idx == len(word)-1:
                return True
            stack.append((x,y))
            res = check(x,y+1,idx+1) or check(x,y-1,idx+1) or check(x-1,y,idx+1) or check(x+1,y,idx+1)
            if res is False:
                stack.pop()
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack = []
                    flag = check(i,j,0)
                    if flag:
                        break
            if flag:
                break
        return flag
"""
Fast
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(board, i,j,word):
            if board[i][j] == word[0]:
                if len(word) ==1:
                    return True
                board[i][j] = ''
                if (i>0 and search(board, i-1,j,word[1:])):
                    return True
                if (i<len(board)-1 and search(board, i+1,j,word[1:])):
                    return True
                if (j>0 and search(board, i,j-1,word[1:])):
                    return True
                if (j<len(board[0])-1 and search(board, i,j+1,word[1:])):
                    return True
                board[i][j] = word[0]
                return False
            else:
                return False
                
            
        if len(word) == 0:
            return False
        if len(board)*len(board[0]) < len(word):
            return False
        word_dic ={}
        for w in word:
            if w not in word_dic:
                word_dic[w] = 1
            else:
                word_dic[w]+=1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word_dic:
                    word_dic[board[i][j]] -=1
        for w in word_dic:
            if word_dic[w] > 0:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(board, i,j,word):
                        return True
        return False