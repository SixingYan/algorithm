"""
187. Repeated DNA Sequences
Medium

394

153

Favorite

Share
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
"""
Comments
10个一组地来遍历，用集合来实现快速查找
更快的方法是用字典
"""
"""
My
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = set([])
        if len(s) < 11:
            return list(seq)
        seqd = set([])
        for i in range(len(s)-9):
            sq = s[i:i+10]
            if sq in seq:
                continue
            if sq in seqd:
                seq.add(sq)
            else:
                seqd.add(sq)
        return list(seq)
                
"""
Fast
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)
        dict = {}
        stack = []
        for i in range(n - 9):
            s_temp = s[i: i + 10]
            if s_temp in dict:
                if s_temp not in stack:
                    stack.append(s_temp)
            else:
                dict[s_temp] = True
        return stack