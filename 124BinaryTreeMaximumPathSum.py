"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
"""
Comments
这个直接看了讨论
内部循环是分别找到左路最大路径长，以及 右路最大路径长。
关键点在于：
	- 当前的最大路径长是max(左,右)+当前
	- 而积累的最大路径总和是 longest=max(longest, 左+右+当前)
所以内部递归和最终得出的结果不是同一个变量

fast 多加了路径长是否大于0的判断
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

    def maxPathSum(self, root: TreeNode) -> int:
        maxpath = [float('-inf')]

        def dfsum(node):
            if node is None:
                return 0
            l = max(0, dfsum(node.left))
            r = max(0, dfsum(node.right))
            maxpath[0] = max(maxpath[0], l + r + node.val)
            return max(l, r) + node.val
        dfsum(root)
        return maxpath[0]
"""
Fast
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        r = float("-inf")
        
        def dfs(node):
            nonlocal r
            val = node.val
            cur = val
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)
                if left > 0:
                    cur += left
            if node.right:
                right = dfs(node.right)
                if right > 0:
                    cur += right
            if right > left:
                left = right
            if left > 0:
                val += left
            if cur > r:
                r = cur
            return val
                
        dfs(root)
        return r