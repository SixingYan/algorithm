"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
"""
Comments
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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is not None:
            while head is not None and head.val == val:
                head = head.next
        else:
            return None
        node = head
        while node is not None:
            while node.next is not None and node.next.val == val:
                node.next = node.next.next
            node = node.next
        return head
"""
Fast
"""
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        while p and p.val==val:
            p = p.next
        head = p
        pre = None
        while p:
            if p.val==val:
                pre.next  = p.next
            else:
                pre = p
            p = p.next
        return head