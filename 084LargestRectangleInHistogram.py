"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
"""
Comments
My的解法是看discuss的，和container装水问题有点像，理解起来比较直观。
关键点在于坐标跳跃的地方，那里用到了dp的思想
"""
"""
My
"""


class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:
            return 0
        if len(heights) == 1:
            return heights[-1]
        # 主要思路是，当前位置能包含的面积，是它左边连续比它大的矩形数量 与 右边连续比它大的矩形数量 之和 乘以它的高度
        # 两个cache的dp，分别记录左边(含自己)连续比height[i]大于或等于的矩形数量
        # 初始化为全1，因为最开始，如果大于，那么偏移都是1位（就是它本身）
        n = len(heights)
        left = [1] * n
        right = [1] * n
        # 分别从左从右数
        # count left 从左数左边，这边后面的数就可以利用前边的计算结果了
        for i in range(1, n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    # 如果h[i] > h[j], 那么h[i]也会大于h[j]大于的那几个数，所以可以直接跳过那几个数
                    j -= left[j]
                else:
                    break
        # count right 右边也含自己，所以最后计数要减一
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break
        res = float('-inf')
        for i in range(n):
            res = max(res, heights[i] * (left[i] + right[i] - 1))
        return res
"""
Fast
"""


class Solution(object):

    def largestRectangleArea(self, heights):
        s = [(float('-inf'), -1)]
        MAX = 0
        for i, h in enumerate(heights):

            if h == s[-1][0]:
                continue
            if h > s[-1][0]:
                s.append((h, i))
                continue

            while h < s[-1][0]:
                temp = s.pop()
                MAX = max(MAX, (i - temp[1]) * temp[0])

            s.append((h, temp[1]))

        for _s in s:
            MAX = max(MAX, (len(heights) - _s[1]) * _s[0])

        return MAX
