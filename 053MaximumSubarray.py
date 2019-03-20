"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
"""
Comments
divide and conquer DC
Ararry DP (my) 
"""
"""
My
"""


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        import copy
        sums = copy.deepcopy(nums)
        for i in range(1, len(nums)):
                # 从前往后计算是叠加还是重开
            sums[i] = max(sums[i - 1] + sums[i], sums[i])
        return max(sums)
"""
Fast
"""


class Solution:

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        allNegative = True
        # 讨论全是正数的情况
        for num in nums:
            if num > 0:
                allNegative = False
                break
        if allNegative:
            return max(nums)

        sum_so_far = 0
        max_sum = float("-inf")
        for i, num in enumerate(nums):
            sum_so_far += num
            if sum_so_far < 0:
                sum_so_far = 0
            max_sum = max(max_sum, sum_so_far)

        return max_sum
