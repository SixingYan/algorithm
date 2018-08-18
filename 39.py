"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
  ● All numbers (including target) will be positive integers.
  ● The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        avaliable = [v for v in candidates if v <= target]
        
        result = []
        while avaliable != []:
            newAvaliable = []
            newResult = []
            if len(result) == 0:
                for c in avaliable:
                    if c < target:
                        newResult.append([c])
                        newAvaliable.append(c)
                    elif c == target:
                        newResult.append([c])
                    else:
                        pass
            else:
                for r in result:
                    if sum(r) == target:
                        newResult.append(r[:])
                        continue
                    
                    for c in avaliable:
                        if (sum(r) + c) <= target:
                            newResult.append(r+[c])
                            newAvaliable.append(c)
                        
            avaliable = list(set(newAvaliable))[:]
            result = newResult[:]
            
        result = list(set(tuple(sorted(r)) for r in result if sum(r) == target))
        return [list(r) for r in result]
"""
Fast
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self._combinationSum(candidates, target, 0, [], ans)
        return ans
    
    def _combinationSum(self, candidates, target, pos, path, ans):
        for i in range(pos, len(candidates)):
            person = candidates[i]
            if target == person:
                ans.append(path+[person])
                return
            elif target == person*2:
                ans.append(path + [person,person])
            elif target < person:
                return
            elif target > person*2:
                self._combinationSum(candidates, target-person, i, path+[person], ans)