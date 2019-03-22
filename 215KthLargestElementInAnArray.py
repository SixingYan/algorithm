"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
"""
Comments
这里用了分治的做法，其实相当于修改了快速排序的方法，如果排序后pos的正确位置就是k-1，那么他就是第k大的元素

最快的方式还是先排序，然后直接给出答案。
"""
"""
My
"""


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickp(left, right):
            begin = left
            end = right
            pos = nums[left]
            while left < right:

                while left < right and nums[right] < pos:
                    right -= 1
                if left < right:
                    nums[left] = nums[right]
                    left += 1

                while left < right and nums[left] >= pos:
                    left += 1
                if left < right:
                    nums[right] = nums[left]
                    right -= 1

            if left == k - 1:
                return pos
            else:
                nums[left] = pos
                if left > k - 1:
                    end = left - 1
                else:
                    begin = left + 1
                return quickp(begin, end)
        return quickp(0, len(nums) - 1)
"""
Fast
"""
from heapq import *


class Solution:

    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        heapify(nums)
        return nlargest(k, nums)[-1]
