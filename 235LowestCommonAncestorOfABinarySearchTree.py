"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
"""
Comments
Fast的方法是递归找到一个node，该节点的值介于p和q之间，这就是两者的最低祖先。这像是一个性质
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 后根搜索 深度优先 当搜索到p时就停止
        order1 = self.DFS(root, p)
        # 后根搜索 深度优先 当搜索到q时停止
        order2 = self.DFS(root, q)
        # 遍历两个路径，找到最后一个相同的val，就是target了
        idx = 0
        while idx<min(len(order1), len(order2)):
            if order1[idx].val == order2[idx].val:
                idx += 1
            else:
                break
        return order1[idx-1]   
    def DFS(self, root, target):    
        order = []
        while root:
            order.append(root)
            if root.val == target.val:
                break
            if root.val < target.val:
                root = root.right
            else:
                root = root.left
        return order
"""
Fast
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root