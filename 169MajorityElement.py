"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
"""
Comments
"""
"""
My
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        最快的例子是排序后，直接找中间的元素
        # 这个方法有点不行的例子 [2,2]
        # 一开始right=1->0，停止循环，left还是0，而target=1
        # 下一次循环, 0<0 不满足条件，停止循环直接返回0，而target还是1
        # 这样就陷入了无限循环的状态
        n = len(nums)
        target = n // 2
        def partition(left, right):
            pos = nums[left]
            while left<right:
                while left<right and nums[right] >= pos:
                    right -= 1
                if left < right:
                    nums[left] = nums[right]
                    left += 1
                while left<right and nums[left] < pos:
                    left += 1
                if left < right:
                    nums[right] = nums[left]
                    right -= 1
            nums[left] = pos
            return left 

        begin = 0
        end = n-1
        while True:
            i = partition(begin, end)
            if i == target:
                break
            elif i < target:
                end = i-1
            else:
                begin=i+1
        x = nums[target]
        '''
        times = 0
        x = nums[0]
        for n in nums:
            if times == 0:
                times = 1
                x = n
            else:
                if n == x:
                    times += 1
                else:
                    times -= 1
        return x
"""
Fast
"""
class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        
        List = nums
        List.sort()
        return List[len(nums)//2]