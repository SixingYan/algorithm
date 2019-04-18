"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
"""
Comments
这个方法是直接看discussion 的，使用二分搜索，关键点在于右侧的指针移动的方式
因为可能含有重复元素，所以右侧指针不能直接移动到 mid-1前面，每次只能缩减到right->mid
如果中间和右侧相等的时候，说明从mid~right都是同一个数，也不能直接跳过这个数，因为这个数可能已经是最小的了
此时只能让右侧前移一个位置 right->right-1
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
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            # 去找非严格递增的那一侧的，不断逼近直到那一侧也严格递增了
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]: # 有可能[mid]位是重复的元素，此时有可能已经是最小的了，所以不要直接跳过，
                right = mid # 不能移到mid前
            else: #有可能是重复的元素，此时不能直接跳过这个数，因为这个数可能已经是最小的
                right -= 1 # right 前移一位
        return nums[left] # 用左侧去逼近
"""
Fast
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        mid = 0
        
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi -= 1
        return nums[lo] 