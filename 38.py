"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        m = {1:'1', 2: '11', 3: '21', 4: '1211', 5: '111221'}
        # 与栈顶不同，把栈弹出所有，放入
        # 如果与栈顶相同，放入
        # 如果没有了，把栈弹出所有
        if n < 6:
            return m[n]
        else:
            base = m[5]
            for _ in range(5,n):
                base = self.change(base)
            return base

    def change(self, base):
        res = ''
        stack = []
        i = 0
        while i < len(base):
            if len(stack) != 0:
                if base[i] != stack[-1]:
                    res += (str(len(stack))+str(stack[0]))
                    stack = []
            stack.append(base[i])
            i += 1
            
        if stack != []:
            res += (str(len(stack))+str(stack[0]))
        
        return res
"""
Fast
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre = "1"
        
        while n - 1 > 0:
            curr = ""
            prec = pre[0]
            cnt = 1
            for _ in pre[1:]:
                if _ == prec:
                    cnt += 1
                else:
                    curr += str(cnt) + prec
                    prec = _
                    cnt = 1
            curr += str(cnt) + prec
            pre = curr
            n -= 1
            
        return pre