"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_ = nums1[:m]
        aLen = m
        bLen = n

        nums = [0 for _ in range(m+n)]
        i = 0
        j = 0
        k = 0
        while i < aLen and j < bLen:
            if nums1_[i] < nums2[j]:
                nums[k] = nums1_[i]
                i += 1
                k += 1
            else:
                nums[k] = nums2[j]
                j += 1
                k += 1
        while i < aLen:
            nums[k] = nums1_[i]
            k += 1
            i += 1
        while j < bLen:
            nums[k] = nums2[j]
            k += 1
            j += 1

        for l in range(m + n):
            nums1[l] = nums[l]
"""
Fast
"""
		while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]