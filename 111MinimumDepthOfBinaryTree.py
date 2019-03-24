"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
"""
Comments
与直接找最大不同的地方是，有可能出现0的情况，所以要先看是不是为0，
为0就用 left+right+1 因为0不影响结果
不为0就用min

Fast 使用的是非递归的广度优先搜索，先判断（是否非空）再入队列
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

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return (left * right == 0 and left + right + 1 or min(left, right) + 1)
"""
Fast
"""


class Solution:

    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp.left is None and temp.right is None:
                    return depth
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return depth
