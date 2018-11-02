23
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def function():
        pass


        # visit around
        lists = [l for l in lists if l is not None]
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        vd = {}
        for i in range(len(lists)): 
            lst = lists[i]
            while lst is not None:
                ky = lst.val
                if not ky in vd.keys():
                    vd[ky] = [lst, lst]
                else:
                    vd[ky][1].next = lst
                    vd[ky][1] = vd[ky][1].next
                lst = lst.next
                vd[ky][1].next = None

        vl = sorted(list(vd.items()),key=lambda v: v[0])
        head = vl[0][1][0]
        for i in range(1, len(vl)):
            t = vl[i-1][1][1]
            t.next = vl[i][1][0]
            t = t.next
        return head












    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None

        main = lists[0]
        for i in range(1, len(lists)):
            main = self.merge(main, lists[i])

        return main

    def merge(self, a, b):
        if a is None and b is None:
            return None
        if a is None and b is not None:
            return b
        if a is not None and b is None:
            return a
        
        if a.val < b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next
        t = head

        while a is not None and b is not None:
            if a.val < b.val:
                t.next = a
                a = a.next
            else:
                t.next = b
                b = b.next
            t = t.next
        while a is not None:
            t.next = a
            a = a.next
            t = t.next
        while b is not None:
            t.next = b
            b = b.next
            t = t.next

        return head


    def ():
        lists = [l for l in lists if l is not None]
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        
        # set head
        sorted(lists, key=lambda v: v.val)
        head = lists[0]
        lists[0] = lists[0].next
        if lists[0] is None:
            del lists[0]
        t = head
        sorted(lists, key=lambda v: v.val)
        # visit
        while len(lists) > 0:
            for i in range(len(lists)):
                t.next = lists[i]
                lists[i] = lists[i].next
                t = t.next
            lists = [l for l in lists if l is not None]
            sorted(lists, key=lambda v: v.val)
        return head



67
    def function():

        result = []
        # 反转
        # a 为大 b 为小
        # 从小的开始
        sm, lg = self.markSmallBig(a, b)
        # sm[i]+lg[i]+next 相加大于1，next=1, 否则next=0
        n = 0

        i = 0
        j = 0
        while i < len(sm):
            value = sm[i] + lg[i] + n
            if value > 1:
                n = 1
            else:
                n = 0

            v = value % 2
            result.append(v)
            i += 1
            j += 1

        while j < len(lg):
            value = lg[j] + n
            if value > 1:
                n = 1
            else:
                n = 0

            v = value % 2
            result.append(v)
            j += 1

        result.reverse()

        return ''.join([int(r) for r in result])

    def markSmallBig(self, a, b):
        a = str(a)
        b = str(b)

        a.reverse()
        b.reverse()

        if len(a) > len(b):
            return b, a
        else:
            return a, b


class ():

    def function():

        total = self.arrP(nums)
        for n in nums:
            if total ^ n >= total:
                return n

    def arrP(self, nums):
        res = nums[0]
        for n in nums[1:]:
            res ^= nums[n]
        return res


# 268
class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

    def function():
        nums.sort()

        nums[len(nums) - 1]

        if nums[0] != 0:
            value = 0

        else:
            for i in range(len(nums) - 1):
                if nums[i] + 1 < nums[i + 1]:
                    value = nums[i] + 1
                    break
        return value

        # fenpian

        sum() < self.gaosi(nums)

    def gaosi(self, nums):
        nums[0] + nums[]) * /2


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg=arg

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # i=0
        # i+1 +1 +1 直到 product 下降
        # 取最新的一个
        #


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        maxP=nums[0]
        i=0
        while i < len(nums):

            oldP=nums[i]
            flag=False
            while (i < len(nums) - 1) and (oldP * nums[i + 1] >= oldP):
                oldP=oldP * nums[i + 1]
                i += 1
                flag=True

            if maxP < oldP:
                maxP=oldP

            if flag is False:
                i += 1

        return maxP

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        s, z, l, sIdx, zIdx, lInx=self.countNum(nums)

        if s == 0 and z == 0:     # only larger
            value=self.arrProduct(nums)

        elif s == 0 and l == 0:   # only zero
            value=0

        elif s > 0 and l == 0:
            if z > 0:           # smaller and zero
                parts=self.seperateArr(z, zIdx, nums)
                value=self.maxProductNoTarget(parts, True)

            else:               # only smaller
                value=self.arrProduct(nums)

        elif s > 0 and l > 0:                  # smaller and larger
            parts=self.seperateArr(s, sIdx, nums)
            value=self.maxProductNoTarget(parts, False)

        elif l > 0 and s > 0:                  # larger and zero
            parts=self.seperateArr(s, sIdx, nums)
            value=self.maxProductNoTarget(parts, True)

        else:                   # smaler zero larger
            if s % 2 == 0:
                value=self.arrProduct(nums)
            else:
                parts=self.seperateArr(z, zIdx, nums)
                value=self.maxProductNoTarget(parts, True)

        return value

    def seperateArr(self, n, nIdx, nums):
        parts=[]

        parts.append(nums[:nIdx[0]])

        if n > 1:
            for i in range(1, n - 1):
                parts.append(nums[nIdx[i]:nIdx[i + 1]])

        parts.append(nums[nIdx[n - 1]:])

        return parts


    def countNum(self, nums):
        s, z, l=(0, 0, 0)
        sIdx=[]
        zIdx=[]
        lInx=[]
        for i in range(len(nums)):
            if nums[i] < 0:
                s += 1
                sIdx.append(i)
            elif nums[i] > 0:
                l += 1
                lInx.append(i)
            else:
                z += 1
                zIdx.append(i)

        return s, z, l, sIdx, zIdx, lInx

    def maxProductNoTarget(self, numsList, isZero):
        total=1
        maxVList=[]

        for nums in numsList:

            if isZero is True:
                value=self.arrProduct([n for n in nums if n != 0])

            else:
                value=self.arrProduct([n for n in nums if n > 0])
            maxVList.append(value)

        return max(maxVList)


    def arrProduct(self, nums):
        total=1

        for i in range(0, len(nums)):
            total *= nums[i]

        return total


    def productSmaller(self, nums):
        a=self.arrProduct(nums[1:])
        b=self.arrProduct(nums[0:-1])
        if a > b:
            return a
        else:
            return b




pair={}
pair[')']=[]
pair['(']=[]

pair=[]
pair.append('(')


for i in range(1, n):
    tmp=[]
    for j in range(len(pair)):
        if pair[j][-1] == ')':
            pair[j] += '('
        else:
            pair[j] += '('
            tmp.append(pair + ')')
    pair.extend(tmp)
return pair


class Solution:

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.swd(nums)

    def swd(self, nums):
        .append([])
        .append(nums)
        for i in range(2, len(nums)):
            while i > 0:
                for
                i -= 1

            for range(i, len(nums) - i):

            while:

            .append([nums[i]])

    def swd
        return


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            return self.dd(head)

    def dd(self, node):
        last=None
        while last == None and not node == None:
            flag=False
            while not node.next == None and node.val == node.next.val:
                node=node.next
                flag=True
            if not flag:
                last=node
            else:
                node=node.next
        # 判断 [1] [1,1] [1,1,2] [1,1,2,2], [1,1,2,2,3]

        # 判断 [1,2,2,3]
        head=last
        while not last == None and not node == None:
            flag=False
            while not node.next == None and node.val == node.next.val:
                node=node.next
                flag=True
            if flag:
                last.next=node.next
            else:
                last.next=node
            last=last.next
            node=last.next
        return head


class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

    def gp(self, n):
        # num = 0
        # len=0: only (
        # [-1]=): only (
        # [-1]=(:
        ln=n
        rn=n
        p=[]
        p.append('(')
        ln -= 1
        for i in range(1, n):
            tmp=[]
            for j in range(len(pair)):
                if pair[j][-1] == ')':
                    pair[j] += '('
                    ln -= 1
                else:
                    pair[j] += '('
                    tmp.append(pair[j] + ')')

            pair.extend(tmp)
        return pair


length


eat

select startwith a

cantain e t

if yes,
    .pop()
    break

    def ga(self, strs):

        for i in range(len()):


class ClassName(object):
    """docstring for ClassName"""

    def ga(self, strs):
        resDict=collections.defaultdict(list)
        for s in strs:
            count=[0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            resDict[tuple(count)].append(s)
        return [resDict[ky] for ky in resDict.keys()]


length

alen=len(A)
blen=len(B)

import math
if alen < blen:
    num=math.(blen / alen)
num *
sTime=while:

    def function():
        resDict=collections.defaultdict(list)
        for s in strs:
            resDict[tuple(sorted(list(s)))].append(s)
        return [resDict[ky] for ky in resDict.keys()]


nums


str(bin(8))[2:]
    def function():
        if nums
        result=[]
        length=len(nums) + 1
        for i in range(len(nums)):
            indxs=self.genIndx(i, length)
            result.append([nums[i] for i in range(indxs) if indxs[i] == 1])
        list(set(result))

    def genIndx(self, n, strlen):

        return []  # [0,0,1]

        def function(self, n):
            out=[[1]]
            left=n
            right=n
            for i in range(2 * n):
                tem=[]
                for group in out:
                    now=sum(group)
                    if now > 0:
                        if group.count(1) < n:
                            tem.append(group + [1])
                        tem.append(group + [-1])
                    if now=0:
                        tem.append(group + [1])
                group=tem
            return self.tranout(out)

        def tranout(self, arr):
            res=[]
            d={1: '(', -1: ')'}
            for group in out:
                tem=[d[g] for g in group]
                res.append(''.join(tem))
            return res

        if self.ia(s) == self.ia(t):
            return True
        else:
            return False

    def ia(s):
        count=[0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)

    def function(self, digits):
        d={'2': ['a', 'b', 'c', ], '3': ['d', 'e', 'f', ], '4': ['g', 'h', 'i', ],
             '5': ['j', 'k', 'l', ], '6': ['m', 'n', 'o', ], '7': ['p', 'q', 'r', 's', ],
             '8': ['t', 'u', 'v', ], '9': ['w', 'x', 'y', 'z', ]}
        if len(digits) == 0:
            return []
        out = ['']
        for dig in digits:
            tem = []
            for di in d[dig]:
                for ing in out:
                    tem.append(ing + di)
            out = tem
        return out
