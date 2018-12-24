"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def __init__(self):
        self.grid = None
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        # cut edge solution
        # visit
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    num += 1
                    self.judge(i, j)
        return num
    
    def find(self, i, j):
        if i >= len(self.grid) or j >= len(self.grid[0]) or i < 0 or j < 0:
            return 
        if self.grid[i][j] == "1":
            self.judge(i,j)
        else:
            return
        
    def judge(self, i, j):
        self.grid[i][j] = "0"
        self.find(i+1, j)
        self.find(i-1, j)
        self.find(i, j+1)
        self.find(i, j-1)
"""
Fast
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
        """
        count = 0
        pre = []

        for row in range(len(grid)):
            cur = []
            index = 0
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    if grid[row][col-1]=='0' or col==0:
                        cur.append(set([col]))
                        index += 1
                    elif grid[row][col-1]=='1':
                        cur[index-1].add(col)
            
            for j in pre:
                tmp = set()
                for index in range(len(cur)-1,-1,-1):
                    if cur[index]&j:
                        tmp |= cur[index]
                        cur.remove(cur[index])
                if tmp:
                    cur.append(tmp)

            all = set()
            for j in pre:
                all |= j
            
            for i in cur:
                if not i&all:
                    count += 1
                    continue
                overlap = 0
                for j in pre:
                    if i&j:
                        overlap += 1
                count -= max(overlap-1, 0)
            
            pre = cur
        return count