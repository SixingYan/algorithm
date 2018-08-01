"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = 0
        res = l1
        prior = l1

        while l1 is not None and l2 is not None:
            v = l1.val + l2.val + n
            if v > 9:
                n = 1
                v = v - 10
            else:
                n = 0
            l1.val = v
            prior = l1
            l1 = l1.next
            l2 = l2.next

        if l1 is not None and l2 is None:
            while l1 is not None:
                v = l1.val + n
                if v > 9:
                    n = 1
                    v = v - 10
                else:
                    n = 0
                l1.val = v
                prior = l1
                l1 = l1.next

        elif l1 is None and l2 is not None:
            while l2 is not None:
                v = l2.val + n
                if v > 9:
                    n = 1
                    v = v - 10
                else:
                    n = 0
                l2.val = v
                prior.next = l2
                prior = prior.next
                l2 = l2.next

        if n != 0:
            prior.next = ListNode(n)

        return res

"""
Fast
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = l1
        p1, p2 = l1, l2
        while l1 and l2:
            carry1 = carry
            carry = (l1.val + l2.val + carry1) // 10
            l1.val = (l1.val + l2.val + carry1) % 10
            p1 = l1
            l1 = l1.next
            l2 = l2.next
        while l1:
            carry1 = carry
            carry = (l1.val + carry1) // 10
            l1.val = (l1.val + carry1) % 10
            p1 = l1
            l1 = l1.next
        if l2:
            p1.next = l2
        while l2:
            carry1 = carry
            carry = (l2.val + carry1) // 10
            l2.val = (l2.val + carry1) % 10
            p1 = l2
            l2 = l2.next
        if carry:
            p1.next = ListNode(carry)
        return l3
