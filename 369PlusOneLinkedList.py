"""

"""
"""
Comments
Beat 100%
related: 92 328 (microsoft)
company: google

"""
"""
My
"""
'''
123->124
129->130
199->200
99->100
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = head
        # revese list
        head = self.reverse(head)
        # add 
        head = self.add(head)
        # reverse
        return self.reverse(head)

    def reverse(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

    def add(self, head):
        node = head
        p = 1
        while node:
            v = node.val + p
            if v > 9:
                node.val = 0
                p = 1
                if node.next == None:
                    node.next = ListNode(1)
                    break
            else:
                node.val = v
                p = 0 
                break
            node = node.next
        return head
"""
Fast
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(node):
            curr = node
            prev = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        if not head:
            return head
        
        curr = reverse(head)
        carry = 1
        dummy = ListNode(0)
        start = dummy
        while curr or carry:
            x = 0
            if curr:
                x = curr.val
                curr = curr.next
            sums = carry + x
            start.next = ListNode(sums%10)
            start = start.next
            carry = sums/10
        return reverse(dummy.next)