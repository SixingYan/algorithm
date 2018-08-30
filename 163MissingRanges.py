"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
"""
Comments
beat 99%
"""
"""
My
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def getDiff(lar, sml):
            if (lar - sml) == 2:
                return str(sml + 1)
            else:
                return str(sml + 1) + '->' + str(lar - 1)
        if nums == []:
            return [getDiff(upper+1, lower-1)]
        result = []
        start = 0
        if nums[0] != lower:
            result.append(getDiff(nums[0], lower - 1))
            nums = [lower] + nums[:]
            start = 1
            
        for i in range(start, len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            if nums[i + 1] != nums[i] + 1:
                result.append(getDiff(nums[i + 1], nums[i]))
        if nums[-1] != upper:
            result.append(getDiff((upper+1), nums[-1]))
        return result
"""
Fast
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res =[]
        pre = lower-1
        for i in range(len(nums)+1):
            if i == len(nums):
                curr = upper+1
            else:
                curr = nums[i]
            if curr-pre>=2:
                res.append(self.helper(pre+1, curr-1))
            pre = curr
        return res
    def helper(self, start, end):
        if start==end:
            return "{}".format(start)
        else:
            return "{}->{}".format(start,end)