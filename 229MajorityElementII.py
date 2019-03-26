"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
"""
Comments
"""
"""
My
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = [0,0]
        elemt = [None, None]
        for n in nums:
            if n in elemt:
                idx = elemt.index(n)
                count[idx] +=1
            elif 0 in count:
                idx = count.index(0)
                elemt[idx] = n
                count[idx] = 1
            else:
                if count[0] > 0:
                    count[0] -= 1
                if count[0] == 0:
                    elemt[0] = None                    
                if count[1] > 0:
                    count[1] -= 1
                if count[1] == 0:
                    elemt[1] = None
        return [e for e in set(elemt) if nums.count(e) > len(nums) // 3]
"""
Fast
"""
class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]