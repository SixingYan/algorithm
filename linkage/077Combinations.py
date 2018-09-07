"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
"""
Comments
My是combine的标准实现，比较好理解
"""
"""
My
"""
import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        org = [i+1 for i in range(n)]
        result = []
        tmp = [0] * k
        def next_num(li, ni):
            if ni == k:
                result.append(copy.copy(tmp))
                return 
            for lj in range(li, n):
                tmp[ni] = org[lj]
                next_num(lj+1, ni+1)

        next_num(0, 0)
        return result
        
"""
Fast
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        if k > n:
            return []
        
        _b = [i + 1 for i in range(k)]
        i = k - 1
        while True:
            result.append(_b[:])
            if _b[0] == n - k + 1:
                break
                
            for j in xrange(i, -1, -1):
                if _b[j] == n - k + j + 1:
                    continue
                    
                break
            
            _b[j] += 1
            for _i in range(j + 1, k):
                _b[_i] = _b[_i - 1] + 1
            
        return result