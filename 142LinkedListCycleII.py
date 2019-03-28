"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""
"""
Comments

Fast 的做法还是一快（两步）一慢（一步）地走，当两者相遇的时候，说明有环。
s为步速，n为圈数，r为环长度
快指针: 2s = s + nr 慢指针的路程+已经转了n圈
所以慢指针的路程为 s = nr

a 为head到入口的路程，x为入口到相遇的路程，
所以慢指针的路程也可以表达为 s = a + x
所以 a + x = nr
a = nr - x = (n-1)r + (r-x)
也就是说，a = head到入口的路程 = 转了n-1圈环 + 相遇后继续走完环剩下的距离
所以此时再从头走个指针，相遇的时候就是 head到入口的路程了
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set([])
        node = head
        nodes.add(node)
        while node is not None:
            if node.next in nodes:
                return node.next
            nodes.add(node)
            node = node.next
        return None
"""
Fast
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next

                return fast
        
        return None