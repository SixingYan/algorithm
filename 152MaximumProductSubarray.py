"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        每个数当前的累计，要么是它本身，要么是它和前面序列的累乘的相乘
        因为会有正负，所以同时记录最大和最小（用于记录可能的负值）
        当遇到负数的时候可能会反转
        """
        # mx, mn 当前index之前的序列的最大值，最小值
        # res 返回的乘积最大值
        mx,mn,res = nums[0],nums[0],nums[0]
        for i in range(1, len(nums)):
            tmpx, tmpn = mx, mn
            mx = max(nums[i], max(nums[i]*tmpx, nums[i]*tmpn))
            mn = min(nums[i], min(nums[i]*tmpx, nums[i]*tmpn))
            res = max(res, mx)
        return res
"""
Fast
"""
import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(start, end, step):
            max_end = 1
            min_end = 1
            maxm = -sys.maxsize
            for i in range(start, end, step):
               
                max_end *= nums[i]
                if max_end > maxm:
                    maxm = max_end
                if max_end == 0:
                    max_end = 1
            return maxm
        left_max = helper(0, len(nums), 1)
        right_max = helper(len(nums) - 1, -1, -1)
        return max(left_max, right_max)
        