"""
 Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""
"""
Comments
"""
"""
My
"""
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        self.dd(head)
        return tmp
    def dd(self, head):
        while not head == None:
            if not head.next == None and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
"""
Fast
"""
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p != None:
            while p.next != None and p.val == p.next.val :# 直接在这里遍历
                p.next = p.next.next
            p = p.next
        return head