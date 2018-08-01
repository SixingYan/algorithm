"""
141.Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        flag = False
        while node is not None:
            if node.next == head:
                flag = True
                break
            tem = node.next
            node.next = head
            node = tem
        return flag
"""
Fast
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            normalSpeed = head
            x2Speed = head.next
            while normalSpeed is not x2Speed:
                normalSpeed = normalSpeed.next
                x2Speed = x2Speed.next.next
            return True
        except:
            return False