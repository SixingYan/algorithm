"""
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?

"""
"""
Comments
"""
"""
My
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        w = str(bin(n))[2:]
        if len(w) < 32:
            w = '0' * (32-len(w)) + w
        return self.change(list(w))
    
    def change(self, s):
        for i in range(int((len(s)-1)/2)+1):
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
        return int(''.join(s),2)
"""
Fast
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(("{:032b}".format(n))[::-1],2)