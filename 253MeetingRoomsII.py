"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
"""
Comments
遍历
    if 当前会议开始时间 < 正在进行的会议的结束时间
        多一个会议室
    else
        下一个正在进行的会议
"""
"""
My
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class node(object):

    def __init__(self, inter):
        self.inter = inter
        self.children = []


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        points = []
        for p in intervals:
            points.append((p.start, 1))
            points.append((p.end, -1))
        ongoing = 0
        maxMeeting = 0
        for p in sorted(points):
            ongoing += p[1]
            maxMeeting = max(maxMeeting, ongoing)

        return maxMeeting

    def minMeetingRooms2(self, intervals):
        minHeap = MinHeap(intervals[0])
        for p in intervals[1:]:
            if p.start < MinHeap.getMin():
                MinHeap.add(p.end)
            else:
                MinHeap.put(p.end)


class MinHeap(object):

    def __init__(self, val):
        self.data = [val]

    def getMin(self):
        return self.data[0]

    def add(self, val):
        j = 0
        while True:
            left = (j + 1) * 2 - 1
            i = left
            if left != len(self.data) - 1 and self.data[left] > self.data[left + 1]: # find the smaller
                i += 1 
            if val < self.data[i]:# put down the larger
                val, self.data[i] = self.data[i], val
            
            if left == len(self.data) - 1: # add
                self.data.append(val)
                break
            else: # find the child
                j = i

    def put(self, val):
        # put down
        self.data[0] = val
        j = 0
        cur = self.data[0]
        while True:
            left = (j + 1) * 2 - 1
            i = left
            if left != len(self.data) - 1 and self.data[left] > self.data[left + 1]:
                i += 1
            if cur > self.data[i]:
                self.data[j] = self.data[i]
                j = i
            else:
                break


"""
Fast
"""
"""
Solution 1:

1. Grab all the start times and sort 
2. Grab all end times and sort
3. Set a compare variable that tracks the end times and set it to the 1st end time.
4. Iterate over the startime and if the start time is lesser than the end time then increment meeting rooms
5. Else, increment the compare variable by 1



Solution 2: HEAP
1. Sort the intervals based on the start time
2. Create an empty heap list to store the end times of the intervals
3. Iterate over the interval, if the heap is not empty and if the current start time is greater than heap[0], heapreplace with current's end time. 
Meaning, the start times and the end time do not clash.
4. Else, push the end time of the current interval to the heap. Meaning, the meetings will clash and we need to update the heap with the end time of the current meeting.
5. Return the length of the heap.

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        starttimes = [x.start for x in intervals]
        endtimes = [x.end for x in intervals]
        starttimes.sort()
        endtimes.sort()
        rooms = 0
        endmeet = 0

        for i in starttimes:
            if i < endtimes[endmeet]:
                rooms += 1
            else:
                endmeet += 1
        return rooms

    """
    def minMeetingRooms(self, intervals):    
        import heapq
        heap = []
        
        intervals.sort(key=lambda x:x.start)
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        
        return len(heap)
        
    """
