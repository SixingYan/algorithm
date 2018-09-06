"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
"""
"""
Comments 不用递归，用循环
"""
"""
My
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fbv(1,n)
    def fbv(self, left, right):
        if not left < right:
            return left
        cent = int((left + right)/2)
        if isBadVersion(cent):
            return self.fbv(left, cent)
        else:
            return self.fbv(cent+1, right)
"""
Fast
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        checking = (end + start)/2
        while (end != start):  #停止条件是两者相等，和我一样
            if isBadVersion(checking):
                end = checking
            else:
                start =  checking + 1
            checking = (end+start)/2
        
        return start