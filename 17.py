"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':['a','b','c',],'3':['d','e','f',],'4':['g','h','i',],
        '5':['j','k','l',],'6':['m','n','o',],'7':['p','q','r','s',],
        '8':['t','u','v',],'9':['w','x','y','z',]}
        if len(digits) == 0:
            return []
        out = ['']
        for dig in digits:
            tem = []
            for di in d[dig]:
                for ing in out:
                    tem.append(ing + di)
            out = tem
        return out
"""
Fast
"""
dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        None: None}

class Solution(object):
    def letterCombinations(self, digits):
        # DFS
        result = []
        ls = len(digits)
        if ls == 0:
            return result
        current = digits[0]
        posfix = self.letterCombinations(digits[1:])
        for t in dmap[current]:
            if len(posfix) > 0:
                for p in posfix:
                    temp = t + p
                    result.append(temp)
            else:
                result.append(t)
        return result