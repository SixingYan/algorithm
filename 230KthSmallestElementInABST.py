"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


"""
"""
Comments
这题是看了讨论的
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
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 它的衍生问题可以是，如何把BST转化为排好序的数组
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while k!=0:
            node = stack.pop()
            k-=1
            if k == 0:
                return node.val
            node = node.right
            while node:
                stack.append(node)
                node=node.left
                
        return -1
"""
Fast
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        curr = root
        l = []
        while curr or (k > 0):
            while curr:
                l.append(curr)
                curr = curr.left
            curr = l.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            