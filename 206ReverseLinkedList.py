"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
"""
Comments
循环的方法也是看discuss的
"""
"""
My
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
"""
Fast
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head, new_tail = self.reverse(head)
        return new_head
    
    def reverse(self, node):
        if not node:
            return None, None
        elif not node.next:
            return node, node
        else:
            head, tail = self.reverse(node.next)
            tail.next = node
            node.next = None
            return head, node