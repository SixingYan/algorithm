"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
"""
Comments
"""
"""
My
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if self.theSame(p, q) is True:
            if p is None:
                return True
        else:
            return False

        return self.verifyTwo(p, q)

    def verifyTwo(self, tr1, tr2):
        if tr1.val == tr2.val:
            if (self.theSame(tr1.right, tr2.right) and self.theSame(tr1.left, tr2.left)) is False:
                return False

            if tr1.right is not None:
                r = self.verifyTwo(tr1.right, tr2.right)
                if r is False:
                    return False

            if tr1.left is not None:
                r = self.verifyTwo(tr1.left, tr2.left)
                if r is False:
                    return False

            return True

        else:
            return False

    def theSame(self, n1, n2):
        if n1 is not None and n2 is not None:
            return True

        if n1 is None and n2 is None:
            return True

        return False

"""
Fast
"""
class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
