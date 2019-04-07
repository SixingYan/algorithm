"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
"""
Comments 
My是看答案写的，greedy解法，每次更新最大能跳到的距离。n^2的复杂度会超时
Fast的解法是从后向前，速度会快一半，应该是试到一半就会出答案了
"""
"""
My
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx, n = 0, len(nums)
        for i,x in enumerate(nums):
            if mx < i:
                return False
            if mx >= n-1:
                return True
            mx = max(mx, i+x)
"""
Fast
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        min_successful_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= min_successful_index:
                min_successful_index = i

        return min_successful_index == 0