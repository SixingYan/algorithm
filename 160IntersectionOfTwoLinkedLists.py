"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
"""
Comments
最后return的地方，那样写才不会 time limit exceed

Fast 方法
计数A和B的长度（假设A长）
那么先让A走|A|-|B|步，然后A，B再同时走，直到两者的node相同，此时就是相交点

另：如果只是判断是否有相交的点，就是上面的方法中，如果一直到结尾都不出现相同，就是没有相交点
"""
"""
My
"""


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        na = headA
        nb = headB
        d = set([])
        a = 0
        b = 0

        while na is not None:
            d.add(na.val)
            na = na.next
            a += 1

        key = None
        while nb is not None:
            if key is None and nb.val in d:
                c = ListNode(nb.val)
                c.next = nb.next
                key = nb.val
            nb = nb.next
            b += 1

        if key is None:
            return None

        if a > b:
            return c
        else:
            na = headA
            while na is not None:
                if na.val == key:
                    return na
                na = na.next
"""
Fast
"""


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = lenB = 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        if lenA < lenB:
            for i in range(lenB - lenA):  # "shorten" longer list
                headB = headB.next
        elif lenB < lenA:
            for i in range(lenA - lenB):
                headA = headA.next
        currA, currB = headA, headB
        while currB != currA:
            currA = currA.next
            currB = currB.next
        return currA
