class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        """
        [1,1]
        [1,1]
        [1,1]

        [1,1,1,1]
        [1,1,1,1]
        """
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1 or n == 1:
            return True
        
        if m > n:
            lm = rm = m
            for i in range(lm):
                [matrix[i+j][i+j] for j in range(n)]
                


        else:



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.analysis(list(s)) == self.analysis(list(t))
        
    def analysis(self, s):
        arr = []
        d = {}
        idx = 0
        for i in range(len(s)):
            if s[i] in d.keys():
                arr.append(d[s[i]])
            else:
                d[s[i]] = idx
                arr.append(idx)
                idx += 1

        return arr





class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
    
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        pop_part = []
        mul_start = -1
        mul_start_idx = -1
        for i in range(len(source)):

            if "*/" in cur:



            if mul_start != -1:
                source[i] = ""
                continue

            cur = source[i]
            if "/*" in cur:
            if "//" in cur:
























