"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
Comments
这题练习过
"""
"""
My
"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        def dfs(bg, ed):
            if bg >= ed:
                ret.append(nums[:])
            else:
                i = bg
                for j in range(bg, ed):
                    nums[i], nums[j] = nums[j], nums[i]
                    dfs(bg + 1, ed)  # begin 往前推
                    nums[i], nums[j] = nums[j], nums[i]
        dfs(0, len(nums))
        return ret

"""
Fast
"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        x = self.permute(nums[1:])
        res = []
        for after in x:
            for i in range(len(after) + 1):
                res.append(after[:i] + [nums[0]] + after[i:])
        return res
