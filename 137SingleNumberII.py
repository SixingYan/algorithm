"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
"""
Comments
我的方法是排序后每三个检查一次，或者用defaultdict来计数
Fast 的方法用了计数类 Counter
"""
"""
My
"""


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        '''
        nums = sorted(nums)
        for i in range(0,len(nums),3):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
        '''
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] == 3:
                d.pop(n, None)
        for k in d.keys():
            return k
"""
Fast
"""
from collections import Counter


class Solution:

    def singleNumber(self, nums: 'List[int]') -> 'int':
        s = Counter(nums)

        for key in s:
            if s.get(key) == 1:
                return key
