"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = self.link2list(l1, l2)
        s = list(str(s))

        head = ListNode(s[0])
        node = head
        for j in range(1, len(s)):
            node.next = ListNode(s[j])
            node = node.next

        return head

    def link2list(self, l1, l2):
        list1 = []
        list2 = []

        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next

        n1 = int(''.join(str(i) for i in list1))
        n2 = int(''.join(str(i) for i in list2))

        return n1 + n2

"""
Fast
"""
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        while l1:
            val1 = val1 * 10 + l1.val
            l1 = l1.next

        val2 = 0
        while l2:
            val2 = val2 * 10 + l2.val
            l2 = l2.next
        total = val1 + val2
        last = None
        if total == 0:
            return ListNode(0)
        while total > 0:
            l = ListNode(total % 10)
            l.next = last
            last = l
            total /= 10
        return last
