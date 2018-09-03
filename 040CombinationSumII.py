"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
"""
Comments
"""
"""
My
"""
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        candidates = [_ for _ in candidates if _ <= target]

        return self.choose(candidates, target)

    def choose(self, candidates, target):
        tmp = []
        result = []
        n = len(candidates)
        def next_num(li=0, ni=0):
            s = sum(tmp)
            if s == target:
                result.append(copy.copy(tmp))
                return 
            if s > target:
                return 
            if ni == n:
                return 
            for lj in range(li, n):
                tmp.append(candidates[lj])
                next_num(lj + 1, ni + 1)
                tmp.pop()
                
        next_num()
        result = [list(s) for s in set([tuple(l) for l in result])]
        return result
"""
Fast
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = {}
        uniCands = []
        for num in candidates:
            if not num in self.nums:
                self.nums[num] = 1
                uniCands.append(num)
            else:
                self.nums[num] += 1
        uniCands.sort()
        print uniCands
        res = []
        
        def dfs(uniCands, target, start, curr):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0:
                return
            for i in range(start, len(uniCands)):
                num = uniCands[i]
                if target < num:
                    break
                cnt = self.nums[num]
                while cnt >= 1 and target>=num:
                    curr.append(num)
                    target -= num
                    dfs(uniCands, target, i+1, curr)
                    cnt -= 1
                ori = self.nums[num]
                while ori > cnt:
                    curr.pop()
                    target += num
                    cnt += 1
        
        dfs(uniCands, target, 0, [])
        return res
