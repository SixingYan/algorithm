"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nDict = {}
        for n in nums:
            if n in nDict.keys():
                nDict[n] += 1
            else:
                nDict[n] = 1
        items = list(nDict.items())
        items.sort(key=lambda p: p[1], reverse=True)
        return [items[i][0] for i in range(k)]
"""
Fast
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cntmap = collections.defaultdict(int)
        for num in nums:
            cntmap[num] += 1
        
        decnt = sorted(cntmap.items(), key=operator.itemgetter(1), reverse=True)
        res = [item[0] for item in decnt[0:k]]
        
        return res
