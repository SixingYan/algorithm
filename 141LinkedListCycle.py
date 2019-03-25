"""
141.Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
"""
Comments
遍历过去，每次把已经遍历的节点的下一个指针指向head，
进入下一个循环，如果发现当前点指向head了，说明它其实指向了之前的某个点，
所以是有循环了。

Fast
用一个快（一次两步）一个慢（一次一步）的两个指针走，如果有环，那么快指针总能遇到慢指针
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