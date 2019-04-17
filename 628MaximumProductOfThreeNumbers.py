"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
"""
Comments

Fast 的解法是用一趟遍历，来不断排列 n1 n2 n3三个数，比较的过程需要精心设计
"""
"""
My
"""


class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def prod3(n):
            return n[0] * n[1] * n[2]
        if len(nums) == 3:
            return prod3(nums)
        nums = sorted(nums)
        return max(prod3(nums[:2] + [nums[-1]]), prod3(nums[:3]), prod3(nums[-3:]))
"""
Fast
"""


class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for n in nums:
            # 看最小两个
            if n < min2:
                if n < min1:  # 连1也要更新
                    min2, min1 = min1, n
                else:  # 只更新2
                    min2 = n
            # 看最大三个
            if n > max3:  # 3要更新
                if n > max2:  # 2也要更新
                    if n > max1:  # 1 也要更新
                        # 相当于三者都得更新
                        max3, max2, max1 = max2, max1, n
                    else:  # 只更新两者
                        max3, max2 = max2, n
                else:  # 只更新3
                    max3 = n
        return max(max1 * max2 * max3, max1 * min1 * min2)
