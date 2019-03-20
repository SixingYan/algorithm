"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        leveldict = defaultdict(list)
        levels = []
        
        def maxdepth(node,k):
            if node is None:
                return 0
            leveldict[k].append(node.val)
            return max(maxdepth(node.left,k+1), maxdepth(node.right,k+1))+1
        depth = maxdepth(root, 0)
        for i in range(depth):
            levels.append(leveldict[i])
        return levels
"""
Fast
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # validate
        if root is None:
            return []
        
        # init
        res = []
        q = [root]
        
        # run bfs
        while q:
            res.append([])
            nxt_q = []
            for node in q:
                res[-1].append(node.val)
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q
        return res
        
        
#         res = []
#         self.dfs(root, 1, res)
#         return res
#      
#     def dfs(self, node, h, res):
#         if node is None:
#             return 
#         if len(res) < h:
#             res.append([])
#         self.dfs(node.left, h + 1, res)
#         res[h-1].append(node.val)
#         self.dfs(node.right, h + 1, res)