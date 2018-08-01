"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = [[1]]
        for i in range(2*n-1):
            tem = []
            for group in out:
                now = sum(group)
                if  now > 0:
                    if group.count(1) < n:
                        tem.append(group + [1])
                    tem.append(group + [-1])
                if now == 0:
                    tem.append(group + [1])
            out = tem
        return self.tranout(out)

    def tranout(self, out):
        res = []
        d = {1:'(',-1:')'}
        for group in out:
            tem = [d[g] for g in group]
            res.append(''.join(tem))
        return res
"""
Fast
"""
class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)