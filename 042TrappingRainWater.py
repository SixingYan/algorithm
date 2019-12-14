"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

https://leetcode.com/problems/trapping-rain-water/

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
"""
Comments
My的方法参考了双指针的方法
Fast 不是最快的，而是使用DP的方法
"""
"""
My
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针的方法
        res = 0
        leftMax = rightMax = 0
        l, r = 0, len(height) - 1
        while l < r:
            # 小的一边先动
            # 左边小于右边
            if height[l] < height[r]:
                if height[l] >= leftMax:  # 取等于号是考虑第一个数
                    leftMax = height[l]
                else:
                    res += (leftMax - height[l])
                l += 1
            # 右边小于左边
            else:
                if height[r] >= rightMax:  # 取等于号是考虑第一个数
                    rightMax = height[r]
                else:
                    res += (rightMax - height[r])
                r -= 1
        return res
"""
Fast
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left2right = [0 for _ in range(len(height))]
        right2left = [0 for _ in range(len(height))]

        for i in range(len(height)):
            if i == 0:
                left2right[i] = height[i]
            else:
            	# 考虑旁边的高度（积累高度），因为旁边比当前高，才能有积水
                left2right[i] = max(left2right[i - 1], height[i])

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right2left[i] = height[i]
            else:
                right2left[i] = max(right2left[i + 1], height[i])

        for i in range(len(height)):
        	# 最后的高度取决于最低的那一档
            water += (min(left2right[i], right2left[i]) - height[i])

        return water
