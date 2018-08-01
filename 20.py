"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""
"""
Comments
"""
"""
My
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        else:
            return self.iv(s)
    def iv(self, s):
        pairs = {'(':')', ')':'(', '{':'}', '}':'{', '[':']', ']':'['}
        heap = []
        for c in s:
            if not len(heap)==0 and heap[-1] == pairs[c]:
                heap.pop()
            else:
                heap.append(c)
        if len(heap) == 0:
            return True
        else:
            return False
"""
Fast
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        deq = deque()
        pair = {'(': ')', '[': ']', '{': '}'}  #因为有顺序，所以可以减少对比的数量
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                deq.append(letter)
            else:
                if len(deq) > 0 and letter == pair[deq[-1]]:
                    deq.pop()
                else:
                    return False
        
        return len(deq) == 0