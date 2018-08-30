"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""
"""
Comments
string
"""
"""
My
"""


class Solution(object):

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        if time == "23:59":
            return "22:22"
        nums = [int(t) for t in time if t != ':']
        if len(set(nums)) == 1:
            return str(nums[0]) * 2 + ':' + str(nums[0]) * 2
        result = nums[:2] + [':'] + nums[2:]
        MM = nums[2:]
        # generate possible MM
        if rMM[1] != max(nums):
            # if there exist larger num than MM-1
            can = [i for i in nums if i > MM[1]]
            if can != []:
                result[4] = min(can)
                return ''.join(str(e) for e in result)
        if MM[0] != 5:
            # if there are larger num than MM-0 and <=5
            can = [i for i in nums if i > MM[0] and i <= 5]
            if can != []:
                result[3] = min(can)
                result[4] = min(nums)
                return ''.join(str(e) for e in result)

        HH = int(''.join(str(e) for e in nums[:2]))
        # generate possible HH

        def gen(nums, n, k, HH):
            result = []
            tem = [0] * k

            def next_num(a, ni):
                if ni == k:
                    result.append(copy.copy(tem))
                    return
                for i in range(len(a)):
                    tem[ni] = a[i]
                    b = a[:]
                    next_num(b, ni + 1)
            c = nums[:]
            next_num(c, 0)
            digs = [int(''.join(str(d) for d in r)) for r in result]
            return [i for i in digs if i < 24 and i > HH]

        digs = gen(nums, 4, 2, HH)
        if digs == []:
            d = str(min(nums))
            return d * 2 + ':' + d * 2
        else:
            newHH = min(digs)
            if newHH < 10:
                newHH = '0' + str(newHH)
            else:
                newHH = str(newHH)
            newMM = ''.join([str(min(nums))] * 2)

            return newHH + ':' + str(newMM)
"""
Fast
"""


class Solution(object):

    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = [int(x) for x in time if x != ':']
        for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed
        return "{:02d}:{:02d}".format(*divmod(ans, 60))
