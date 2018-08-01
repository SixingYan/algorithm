"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
"""
Comments
"""
"""
My
"""
class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.si(nums, target, 0, len(nums) - 1)

    def si(self, nums, target, left, right):
        if not left < right:
            if nums[left] < target:
                return left + 1
            else:
                return left
        cent = int((left + right) / 2)
        if nums[cent] < target:
            return self.si(nums, target, cent + 1, right)
        elif nums[cent] > target:
            return self.si(nums, target, left, cent - 1)
        else:
            return cent

"""
Fast
"""
class Solution:

    def searchInsert(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    return len([i for i in nums if i < target])
