"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val
        if length ==3:
            return head.val == head.next.next.val
        node2 = head
        node1 = None
        # 0~length//2-1 reverse
        pre = None
        for _ in range(0, length//2):
            node1 = node2
            node2 = node2.next
            node1.next = pre
            pre = node1
        # 跳过一个点后，同时比较
        if length % 2 != 0:
            node2 = node2.next
        # 同时比较
        flag = True
        while node1 and node2:
            if node1.val != node2.val:
                flag = False
                break
            node1 = node1.next
            node2 = node2.next
        return flag    
"""
Fast
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """       
#         f = s = head        
#         stk=[]
        
#         while f and f.next:
#             stk.append(s.val)      
#             s = s.next
#             f = f.next.next
        
#         if f:           
#             s = s.next
            
#         while s:
#             top = stk.pop()            
#             if top != s.val:
#                 return False
#             s  = s.next
        
#         return True
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev