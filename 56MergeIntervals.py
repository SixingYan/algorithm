"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
"""
Comments
"""
"""
My
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda inter : (inter.start, inter.end))
        res = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
            p = intervals[i]
            if p.start > cur.end:
                res.append(cur)
                cur = p
            else:
                if p.end > cur.end:
                    cur.end = p.end
            if i == len(intervals)-1:
                res.append(cur)
        return res
        
"""
Fast
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda x: x.start)
        res,n = [],len(intervals)
        start = end = 0
        while start<n:
            mx = intervals[start].end
            while end<n and intervals[end].start <= mx:
                mx = max(mx,intervals[end].end)
                end += 1
            res.append(Interval(intervals[start].start,mx))
            start = end
        return res