"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [l for l in lists if l is not None]
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        vd = {}
        for i in range(len(lists)): 
            lst = lists[i]
            while lst is not None:
                ky = lst.val
                if not ky in vd.keys():
                    vd[ky] = [lst, lst]
                else:
                    vd[ky][1].next = lst
                    vd[ky][1] = vd[ky][1].next
                lst = lst.next
                vd[ky][1].next = None

        vl = sorted(list(vd.items()),key=lambda v: v[0])
        head = vl[0][1][0]
        for i in range(1, len(vl)):
            t = vl[i-1][1][1]
            t.next = vl[i][1][0]
            t = t.next
        return head


"""
Fast
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next
        res.sort()
        dumm = ListNode(0)
        pre = dumm
        for i in res:
            pre.next = ListNode(i)
            pre=pre.next
        return dumm.next