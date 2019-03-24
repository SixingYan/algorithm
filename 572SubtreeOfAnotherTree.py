"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
"""
Comments
基本的思路是，是否和当前节点对应的子树相同，或者左子树，或者右子树。
如果不是的话就继续递归。真正比较的其实只有第一部分，第二第三部分都是在递归

Fast的方法没看懂 似乎只是对内部方法的递归而不是对整个方法的递归
"""
"""
My
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(n1, n2):
            # 它们必须要同时到底部才算相同
            if not n1 and not n2:
                return True
            if n1 and n2:
                if n1.val == n2.val:
                    return isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)
                return False
            return False
        if s is None:
            # 这里只判断s是否为空，是因为下面要使用它的左右节点
            return False
        return isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

"""
Fast
"""


class Solution:

    def isSubtree(self, s, t):
        def compare(s, t, checkEqual):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                if checkEqual:
                    return False
                else:
                    return compare(s.left, t, False) or compare(s.right, t, False)
            else:
                return (compare(s.left, t.left, True) and compare(s.right, t.right, True)) or \
                    compare(s.left, t, False) or compare(s.right, t, False)

        return compare(s, t, False)
