"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
"""
Comments
My的写法是直接用归并排序的方式，归并到第k个数就停止。经典解放是用

"""
"""
My
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            return self.median(nums2)
        elif len(nums2) == 0:
            return self.median(nums1)
        
        if len(nums1) * len(nums2) == 1:
            return float(nums1[-1] + nums2[-1]) / 2

        l = len(nums1) + len(nums2)
        x = (l-1)//2
        if l % 2 == 0:
            y = x + 1
            t1,t2 = self.getTwo(nums1, nums2,x,y)
            t = (t1+ t2) * 0.5
        else:
            t = self.getOne(nums1, nums2,x)
        return t
    def median(self, nums):
        i = (len(nums)-1)%2 
        j = (len(nums)-1)//2 
        if i % 2 == 0:
            return nums[j]
        else:
            return float(nums[j] + nums[j+1]) / 2 
    def getTwo(self, nums1, nums2, x, y):
        t1, t2 = None, None
        idx = -1
        i = 0
        j = 0
        while i<len(nums1) and j < len(nums2) and idx<y and t2 is None:
            idx += 1
            if t1 is None: 
                if idx == x:
                    t1 = nums1[i] if nums1[i] < nums2[j] else nums2[j]
            else:
                if idx == y:
                    t2 = nums1[i] if nums1[i] < nums2[j] else nums2[j]
                    break

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        while i<len(nums1) and idx<y and t2 is None:
            idx += 1
            if t1 is None: 
                if idx == x:
                    t1 = nums1[i]
            else:
                if idx == y:
                    t2 = nums1[i]
                    break
            i += 1

        while j<len(nums2) and idx<y and t2 is None:
            idx += 1
            if t1 is None: 
                if idx == x:
                    t1 = nums2[j]
            else:
                if idx == y:
                    t2 = nums2[j]
                    break
            j += 1
        print((t1,t2))
        return t1, t2

    def getOne(self, nums1, nums2, x):
        idx = -1
        i = 0
        j = 0
        target = None
        while i<len(nums1) and j < len(nums2) and idx<x and target is None:
            idx += 1
            if idx == x:
                target = nums1[i] if nums1[i] < nums2[j] else nums2[j]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        while i<len(nums1) and idx < x and target is None:
            idx += 1
            if idx == x:
                target = nums1[i]
                break
            i += 1
        while j<len(nums2) and idx < x and target is None:
            idx += 1
            if idx == x:
                target = nums2[j]
                break
            j += 1
        return target
"""
Fast
"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0