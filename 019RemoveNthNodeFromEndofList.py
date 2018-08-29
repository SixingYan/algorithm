"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        que = []
        if n == 0:
            return head
        if head == None:
            return head
        
        while node is not None:
            if len(que) == n+1:
                que.pop(0)
            que.append(node)
            node = node.next
        if len(que) == n:
            if n == 1:
                return None
            return que[1]
        
        if len(que) == 1 and n == 1:
            return None
        if len(que) == 2:
            if n == 1:
                que[0].next = None
                return head    
            if n == 2:
                return que[1]
            
        que[0].next = que[2]
        
        return head
"""
Fast
"""
'I am the fastest'