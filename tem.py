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

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 考虑最多能有几个2
        d={'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','10':'',
          '11':'','12':'','13':'','14':'','15':'','16':'','17':'','18':'','19':'','20':'',
          '21':'','22':'','23':'','24':'','25':'','26':'',}
        
        t = len(s)
        maxN = int(s/2)
        for k in range(maxN+1): # 6选2
            nums = [i for i in range([0]*(t-n*2+n))] 
            result = []
            tem = [0] * k
            n = len(nums)
            gen(0, 0)
            get(result)

        def gen(xi, ni):
            if ni == n:
                result.append(copy.copy(tem))
                return 
            for i in range(xi, n):
                tem[ni] = nums[i]
                gen(xi+1, ni+1)
        
        def get(result):
            idx = -1
            for i in range(len(result)):
                 
                result[i]
        














