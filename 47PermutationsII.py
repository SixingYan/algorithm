"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
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
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        tmp = [0]*n
        def next_num(a, ni):
            if ni == n:
                result.append(copy.copy(tmp))
                return
            for li in range(len(a)):
                tmp[ni] = a[li]
                b = a[:]
                b.pop(li)
                next_num(b, ni+1)
        c = nums[:]
        next_num(c, 0)
        return [list(t) for t in set([tuple(l) for l in result])]
        
"""
Fast
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ret = []
        nums.sort()
        seen = collections.defaultdict(int)
        self.helper(nums, ret, [], seen)
        return ret
    
    def helper(self, nums, ret, temp, seen):
        if len(temp) == len(nums):
            ret.append(temp)
        else:
            for i in range(len(nums)):
                if seen[i] or i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                    continue
                seen[i] = 1
                self.helper(nums, ret, temp + [nums[i]], seen)
                seen[i] = 0
                
                
    # private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean [] used){
    # if(tempList.size() == nums.length){
    #     list.add(new ArrayList<>(tempList));
    # } else{
    #     for(int i = 0; i < nums.length; i++){
    #         if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
    #         used[i] = true; 
    #         tempList.add(nums[i]);
    #         backtrack(list, tempList, nums, used);
    #         used[i] = false; 
    #         tempList.remove(tempList.size() - 1);
    #     }