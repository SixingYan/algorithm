"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
  1. You must do this in-place without making a copy of the array.
  2. Minimize the total number of operations.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return 
        zero = []
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zero.append(i)
            elif len(zero) > 0:
                nums[zero[0]] = nums[i]
                nums[i] = 0
                zero.pop(0)
                zero.append(i)
            else:
                pass
"""
Fast
"""
	def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        assert nums is not None
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1