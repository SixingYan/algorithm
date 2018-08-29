    77
ans = []

1
    def function():

        org = [i + 1 for i in range(n)]
        #ans = [[i+1] for i in range(n)]

        for l in range(0, k):
            for i in range()

            new = []
            for i in range(len(ans)):
                for j in range(l, n):
                    new.append(ans[i] + org[j])

            ans = new[:]

        return ans

    def p(self, nums):
        result = []
        n = len(nums)
        tmp = [0] * n

        def next_num(a, ni):
            if ni == n:
                result.append(copy.copy(tmp))
                return
            for lj in range(len(a)):
                tmp[ni] = a[lj]
                b = a[:]
                b.pop(lj)
                next_num(b, ni + 1)

        a = nums[:]
        next_num(a, 0)
        return result


class Solution(object):

    def combine(self, candidates, target):
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        candidates = [_ for _ in candidates if _ <= target]

        total = []
        for i in range(1, n):
            total.extend(self.choose(candidates, target, i))
        return total

    def choose(self, candidates, target, n)
        tmp = []
        result = []
        def next_num(li, ni):
            s = sum(arr)
            if s == target:
                result.append(copy.copy(arr))
                tmp.pop()
                return
            if s > target:
                tmp.pop()
                return
            if ni == n:
                tmp.pop()
                return
            for lj in range(li, n):
                tmp.append(candidates[lj])
                next_num(li + 1, ni + 1)

        next_num()

        return result









def f():
    def a():
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        if : # not passible
            # rearrange
            pass
        else:

        # 




1 2 3 4
1 2 4 3

1 2 4 3
1 


2 3 1


# 确定 2 属于哪一组
1 + (2 3)
2 + (1 3)
3 + (1 2)

# 确定 3 属于哪一组
1 + (3)
3 + (1)

# 确定 1 属于哪一组

0


        idx = []
        org = [i+1 for i in range(len(nums))]

        for i in range(len(nums)):    
            idx.append(org.pop(org.index(nums[i])))
        for i in range(len(nums)-1, -1, -1):
            if idx[i] != 0:
                idx[i] += 1
                break
        for i in range(len(nums)):
            nums[i] = idx[i] * (i+1)




















