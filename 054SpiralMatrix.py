"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
Comments
这个需要特定的解法才行。用的是能控制当前状态的两个数组轮流给值
"""
"""
My
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        results = []
        if matrix == []:
            return []
        R, C = len(matrix), len(matrix[0])

        seen = [[False]*C for _ in range(R)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        r = c = idx = 0
        for _ in range(R * C): # 这里用到了用总数来遍历
            results.append(matrix[r][c])
            seen[r][c] = True
            # 这里做推进
            i, j = r + dr[idx], c + dc[idx]
            if 0<=i<R and 0<=j<C and seen[i][j] is False:
                # 验证范围是否正确
                # 验证下一个是否未见过
                r, c = i, j
            else:
                # 说明用旧的idx 做r + dr[idx], c + dc[idx] 不对
                idx = (idx + 1) % 4
                # 这里重新做r和c
                r, c = r + dr[idx], c + dc[idx] # 改变方向了

        return results
"""
Fast
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        if r == 0:
            return []
        c = len(matrix[0])
        if c == 0:
            return []
        
        rl = 0
        ru = r - 1
        cl = 0
        cu = c - 1
        
        res = []
        while rl <= ru and cl <= cu:
            for i in range(cl, cu + 1):
                res.append(matrix[rl][i])
            rl += 1
            for i in range(rl, ru + 1):
                res.append(matrix[i][cu])
            cu -= 1
            
            if rl <= ru:
                for i in range(cu, cl - 1, -1):
                    res.append(matrix[ru][i])
                ru -= 1
            if cl <= cu:
                for i in range(ru, rl - 1, -1):
                    res.append(matrix[i][cl])
                cl += 1
        return res