"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
"""
Comments
My是看答案写出来的
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        target = sum
        if root is None:
            return []
        results = []
        def DFS(node,path,tg):
            if not node:
                return
            if not node.left and not node.right:
            	# 这个条件我一开始忽略了。它的path是要算到底的
                if tg == target:
                    results.append(path[:])
                return
            if node.left:
                DFS(node.left, path+[node.left.val], tg+node.left.val)
            if node.right:
                DFS(node.right, path+[node.right.val], tg+node.right.val)
        DFS(root, [root.val], root.val)
        return results
"""
Fast
"""
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        path = []
        self.pathSumHelper(root, sum, path, results)
        return results
    
    def pathSumHelper(self, root, sum, path, results):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            path.append(root.val)
            results.append(path[:])
            path.pop()
            return True        
        path.append(root.val)
        left = self.pathSumHelper(root.left, sum, path, results)
        right = self.pathSumHelper(root.right, sum, path, results)
        path.pop()
        return left or right