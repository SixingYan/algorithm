"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
"""
Comments
这个做法是分左右两边哪边是严格递增，然后严格递增就可以找到有序的值
"""
"""
My
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = -1
        if len(nums) == 0:
            return pos
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[left] <= nums[mid]: # 左边是严格递增
                if nums[left] <=target and target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            else: # 右边是严格递增
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return pos
"""
Fast
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)/2
            if target<nums[0]<nums[mid]:
                l=mid+1
            elif target>=nums[0]>nums[mid]:
                r=mid
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid
            else:
                return mid
        return -1