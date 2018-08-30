"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        def gen(start, end):
            if start == end:
                return str(start)
            else:
                return str(start)+'->'+str(end)
        result = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                result.append(gen(start, end))
                start = nums[i]
            
            end = nums[i]
            
            if i == len(nums)-1:
                result.append(gen(start, end))
        return result
"""
Fast
"""
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 1:
            result.append(str(nums[0]))
        start = 0
        end = 1
        while end < len(nums):
            while (end < len(nums) and nums[end] == nums[end-1] + 1):
                end += 1
            s = str(nums[start])
            if end - start > 1:
                result.append(s + "->" + str(nums[end-1]))
            else:
                result.append(s)
            start = end
            end += 1
            if start == len(nums) - 1:
                result.append(str(nums[start]))
        return result