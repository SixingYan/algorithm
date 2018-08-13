"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        nums = []
        node = head
        while node is not None:
            nums.append(node.val)
            node = node.next

        nums.sort()
        node = head
        i = 0
        while node is not None:
            node.val = nums[i]
            node = node.next
            i += 1

        return head
"""
Fast
"""
class Solution(object):
    def sortList(self, head):
        """
        sort list using quick sort
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail = self.get_tail(head)
        head, tail = self.quick_sort(head, tail)
        tail.next = None
        return head
 
    def quick_sort(self, head, tail):
        """
        Sort in place
        :param head:
        :param tail:
        :return:
        """
        if head is not tail:
            head_left, tail_left, head_ref, tail_ref, head_right, tail_right = self.quicksort_partition(head, tail)
            if head_left is None:  # if there is no node in left part after partition
                head = head_ref
            else:
                head_left, tail_left = self.quick_sort(head_left, tail_left)
                head = head_left
                tail_left.next = head_ref
            if head_right is None:  # if there is no node in right part after partition
                tail = tail_ref
            else:
                head_right, tail_right = self.quick_sort(head_right, tail_right)
                tail_ref.next = head_right
                tail = tail_right
        return head, tail
 
 
    def quicksort_partition(self, head, tail):
        reference = tail
        head_ref, tail_ref = reference, reference
        head_left, tail_left, head_right, tail_right = None, None, None, None
 
        sentinel = ListNode(None)  # use sentinel to simplify the code
        sentinel.next = head
        node = sentinel
        while node.next is not tail:
            node = node.next
            if node.val > reference.val:  # put node into right part
                if head_right is not None:
                    tail_right.next = node
                    tail_right = node
                else:  # right part is empty
                    head_right = node
                    tail_right = node
            elif node.val < reference.val:  # put node into left part
                if head_left is not None:
                    tail_left.next = node
                    tail_left= node
                else:  # left part is empty
                    head_left = node
                    tail_left = node
            else:  # put node into reference part
                tail_ref.next = node
                tail_ref = node
        return head_left, tail_left, head_ref, tail_ref, head_right, tail_right
 
    def get_tail(self, node):
        while node.next:
            node = node.next
        return node