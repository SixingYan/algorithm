"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
"""
Comments
Beat 100%
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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head

        # head is large or x
        if head.val >= x:
            samll_flag = False
            cur_node = head
            while cur_node is not None:
                if cur_node.next is not None and cur_node.next.val < x:
                    tem = cur_node.next
                    # move out that node
                    cur_node.next = tem.next
                    # set new head
                    tem.next, head = head, tem
                    samll_flag = True
                    break

                cur_node = cur_node.next

            if samll_flag is False: # no small exist
                return head

        # head is small
        cur_node = head
        
        # find the prior of first large
        first_large_prior = None
        while cur_node is not None:
            if cur_node.next is not None and cur_node.next.val >= x:
                first_large_prior = cur_node
                break
            cur_node = cur_node.next
            
        if first_large_prior is None: # no large
            return head
        if first_large_prior.next is None: # no need to move
            return head
        
        first_large = first_large_prior.next

        # find the rest of samll
        node = first_large_prior.next
        while node is not None:
            if node.next is not None and node.next.val < x:
                # get that small
                tem = node.next
                # remove small 
                node.next = node.next.next
                # put it after prior of first large
                first_large_prior.next = tem
                tem.next = first_large
                # update first large
                first_large_prior = tem
            else:
                node = node.next

        return head
"""
Fast
"""
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None: return None
        h1 = ListNode(None)
        h2 = ListNode(None)
        t1, t2 = h1, h2
        pt = head
        while pt != None:
            if pt.val < x:
                t1.next = pt
                t1 = pt
                pt = pt.next
            else:
                t2.next = pt
                t2 = pt
                pt = pt.next
        t1.next = h2.next
        t2.next = None
        return h1.next