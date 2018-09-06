"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return
        idx = -1
        # from tail to head
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
            
        if len(nums[idx+1:]) > 1 and max(nums[idx+1:]) == nums[idx+1]:
            
            idd =  nums[idx+1:].index(min([i for i in nums[idx+1:] if i>nums[idx]]))
            idd += (idx+1)
            nums[idx], nums[idd] = nums[idd], nums[idx]
            tem = sorted(nums[idx+1:])
            j = 0
            for i in range(idx+1,len(nums)):
                nums[i] = tem[j]
                j += 1
        else:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
"""
Fast
"""
def reverse(nums, idx):
    l = len(nums) - idx 
    for i in range(0, l/2):
        nums[idx + i], nums[l -1- i + idx] = nums[l -1- i + idx], nums[idx +  i]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 0:
            return
        
        idx = len(nums) - 1
        while idx > 0 and nums[idx - 1] >= nums[idx]:
            idx -= 1
        
        if idx == 0:
            reverse(nums, 0)
        
            return
        
        prev_idx = idx - 1
        next_idx = len(nums) - 1
        while next_idx >= idx and nums[next_idx] <= nums[prev_idx]:
            next_idx -= 1
            
        nums[prev_idx],  nums[next_idx] = nums[next_idx], nums[prev_idx]
        reverse(nums, idx)