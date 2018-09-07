"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if True:
            nums = []
            node = head
            while node is not None:
                nums.append(node.val)
                node = node.next

            newNums = []
            for i in range(len(nums)):
                if nums.count(nums[i]) == 1:
                    newNums.append(nums[i])

            node = head
            if len(newNums) > 0:
                for i in range(len(newNums)):
                    node.val = newNums[i]
                    if i == len(newNums) - 1:
                        node.next = None
                    else:
                        node = node.next
            else:
                return None

            return head
"""
Fast
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        new = dummy
        prev = None
        this = head
        while this:
            if this.val == prev:
                pass
            elif (not this.next or this.val != this.next.val):
                new.next = ListNode(this.val)
                new = new.next
                prev = this.val
            else:
                prev = this.val
            this = this.next
        return dummy.next
