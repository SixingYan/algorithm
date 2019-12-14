"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
"""
Comments
稍慢的方法是先排序，nlogn，然后再一路数过去

Fast 和 My 相同
最快的方法，把这个问题看成 检测链表是否有环 的问题，因为出现两个数字相当于就是两个链指向了同一个地方
"""
"""
My
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 这个问题竟然可以看作是 检测链表是否有环
        fast = nums[0]
        slow = nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        p1 = nums[0]
        p2 = slow
        while p1 != p2: # 两者都按正常速度走
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
"""
Fast
"""
