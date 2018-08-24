"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        length = len(s)
        v = ['a','e','o','i','u']
        vList = [i for i in range(len(s)) if s[i].lower() in v]
        vD = {} 
        for i in range(int(len(vList)/2)):
            vD[vList[i]] = vList[len(vList)-i-1]
        
        result = []
        for i in vD.keys():
            s[i], s[vD[i]] = s[vD[i]], s[i]
        return ''.join(s)
        
"""
Fast
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=list(s)
        i,j=0,len(ans)-1
        d={'a','e','i','o','u','A','E','I','O','U'}
        while i<j:
            while i<j and ans[i] not in d: i+=1
            while i<j and ans[j] not in d: j-=1
            if i<j: 
                ans[i],ans[j]=ans[j],ans[i]
                i+=1
                j-=1
        return ''.join(ans)