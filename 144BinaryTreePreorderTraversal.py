"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        values = []
        while root or stack:
            if root is not None:
                values.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return values
"""
Fast
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion with helper:
"""
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        self.helper(root, res)
        return res 
    
    def helper(self, root, res):
        if root is None:
            return [] 
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
"""       

# Recursion without helper:
"""
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
"""
 
"""class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        mid = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        return mid + left + right
"""
"""
class Solution:
    def __init__(self):
        self.res = []
        
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return [] # DO NOT FORGET []! 
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        
        return self.res
"""

# Non-recursion

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        stack = []
        cur = root
        
        while cur or len(stack) > 0:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                cur = node.right
        return res