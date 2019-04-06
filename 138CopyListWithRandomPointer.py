"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:
https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png


Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
"""
"""
Comments
"""
"""
My
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_to_new = {None:None}
        node = head
        while node:
            new = Node(node.val, None, None)
            old_to_new[node] = new
            node = node.next
        node = head
        while node:
            old_to_new[node].next = old_to_new[node.next]
            old_to_new[node].random = old_to_new[node.random]
            node = node.next
        return old_to_new[head]
"""
Fast
"""
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        d={}
        node=head
        while node:
            d[node]=RandomListNode(node.label)
            node=node.next
        node=head
        d[None]=None
        while node:
            d[node].next=d[node.next]
            d[node].random=d[node.random]
            node=node.next
        return d[head]