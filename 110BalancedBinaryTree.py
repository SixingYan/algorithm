"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
"""
Comments
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
    def isBalanced(self, root: TreeNode) -> bool:
        def balDepth(node):
            if node is None:
                return 0
            left = balDepth(node.left)
            right = balDepth(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left,right)+1
        
        return balDepth(root) != -1
"""
Fast
"""
class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        r = True
        def f(node):
            nonlocal r
            if not node:
                return 0
            dl = f(node.left)
            if not r:
                return 0
            dr = f(node.right)
            if abs(dl - dr) > 1:
                r = False
            return max(dl, dr) + 1
        f(root)
        return r