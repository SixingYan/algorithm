"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
"""
Comments
这个题目是某个经典类型
MY直接看答案写的
"""
"""
My
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] >= nums[left]: # 左边是严格递增
                mini = min(mini, nums[left])
                left = mid + 1
            else: # 右边是严格递增
                mini = min(mini, nums[mid])
                right = mid - 1
        return mini
"""
Fast
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<right:
            if nums[left]<nums[right]:#if the nums is ascend
                return nums[left]
            else:
                mid=left+(right-left)/2
                if nums[mid]<nums[right]: #compare the middle value with the right
                    right=mid#when nums[mid]<nums[right],search left part(including the mid)
                else:
                    left=mid+1#the left half is ascend,so search the right part
        return nums[left]