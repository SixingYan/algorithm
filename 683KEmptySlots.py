"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
"""
"""
Comments

我的是参考solution的，维护一个排序结构
"""
"""
My
"""
import bisect
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bloom = []
        for day, f in enumerate(flowers,1):
            i = bisect.bisect(bloom, f)
            for n in bloom[i-(i>0):i+1]:
                if abs(n-f) - 1 == k:
                    return day
            bloom.insert(i, f)
        return - 1
"""
Fast
"""
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        k += 1
        
        bucketSize = (n + k - 1) // k
        minBuckets = [sys.maxsize] * (bucketSize + 1)
        maxBuckets = [-sys.maxsize] * (bucketSize + 1)
        
        for i, flower in enumerate(flowers):
            bucketIndex = flower // k
            if flower < minBuckets[bucketIndex]:
                minBuckets[bucketIndex] = flower
                if bucketIndex > 0 and flower - k == maxBuckets[bucketIndex-1]:
                    return i + 1
            if flower > maxBuckets[bucketIndex]:
                maxBuckets[bucketIndex] = flower
                if bucketIndex + 1 < bucketSize and minBuckets[bucketIndex+1] - k == flower:
                    return i + 1
        
        return -1