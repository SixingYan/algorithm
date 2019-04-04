"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
"""
Comments
My 是标准解法，从两端开始，每次移动短的那边，因为短的改变才会对水的高度有改变
"""
"""
My
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        mx = float('-inf')
        while left < right and left < len(height)-1 and right > 0:
            mn = min(height[left], height[right])
            sq = mn * (right-left)
            mx = max(mx,sq)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx
"""
Fast
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        t = 0
        for i in range(len(height)):
            for j in range(i):
                h = min(height[i], height[j]) * (i-j)
                if h > t:
                    t = h
        return t
        """
        max_width = 0
        left = 0
        right = len(height) - 1
        max_size = max(height)
        while right > left and max_size * (right - left) > max_width:
            width = right - left
            if height[right] >= height[left]:
                min_height = height[left]
                left += 1
            else:
                min_height = height[right]
                right -= 1
            area = min_height * width
            max_width = area if (area > max_width) else max_width
        return max_width