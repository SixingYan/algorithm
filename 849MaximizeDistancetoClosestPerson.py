"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        group = []
        tem = []
        start = 0
        end = 0
        data = [0, -1, 0]
        for i in range(len(seats)):
            if seats[i] == 1: 
                if tem != []:
                    data[2] = i-1
                    data[0] = len(tem)
                    group.append(data[:])
                    tem = []
                    data = [0,-1,0]
            else:
                tem.append(0)
                if data[1] == -1:
                    data[1] = i
                if i == len(seats)-1:
                    data[2] = i
                    data[0] = len(tem)
                    group.append(data[:])
        
        result = []
        for g in group:
            if g[2] == len(seats)-1 or g[1] == 0:
                result.append(g[0])
            else:
                result.append(int((g[0]+1)/2))
        return max(result)
"""
Fast
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxWindow = 0
        pre = -1
        res = -1
        for i in range(len(seats)):
            
            if seats[i]:
                if pre == -1:
                    window = i*2
                else:
                    window = i-pre
                
                if window > maxWindow:
                    res = window // 2
                    maxWindow = window
                pre = i
                
        if seats[-1] == 0:
            res = max(res,len(seats)-1-pre)
            
        return res