#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 07:21:19 2018

@author: alfonso
"""
def alg_func():
    def function():
        """
        范围内，<0 为偶数
        是否含有0
        负数是否为 偶数

        如果含有0就以0为分界
            分界内 按不含有0 处理

        如果不含有0
            负数是否为偶数
                偶数
                    全部乘积最大
                奇数
                    以奇数为分界
                        分界内全部比较
        """

        s, z, l, sIdx, zIdx, lInx = countNum(nums)

        if z > 0:
            parts = self.seperateArr(z, zIdx, nums)
            value = self.maxProductNoTarget(parts, True)

        else:
            if s % 2 == 0:
                value = self.arrProduct(nums)
            else:
                parts = self.seperateArr(s, sIdx, nums)
                value = self.maxProductNoTarget(parts, False)
        return value
    
    def seperateArr(self, n, nIdx, nums):
        parts = []

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
            if n < 0:
                s += 1
                sIdx.append(i)
            elif n > 0:
                l += 1
                lInx.append(i)
            else:
                z += 1
                zIdx.append(i)

        return s, z, l, sIdx, zIdx, lInx

    def maxProductNoTarget(self, numsList, isZero: bool):
        total = 1
        maxVList = []

        for nums in numsList:
            
            if isZero is True:
                value = self.arrProduct([n for n in nums if n != 0])
            
            else:
                value = self.arrProduct([n for n in nums if n > 0])
            maxVList.append(value)
            
        return max(maxVList)
        

    def arrProduct(self, nums):
        total=1

        for i in range(0, len(nums)):
            total *= nums[i]

        return total

def sort_func(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i
        while j > 0 and tmp < nums[j-1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = tmp
    return nums

if __name__ == '__main__':
    nums = [6, 1, 2, 3, 4, 3, 8, 2, 45, 23, 6534, 64, 4, 32, 34, 53, 22]
    if sort_func(nums) == sorted(nums):
        print('right !!!!!')
    else:
        print('wrong !!!!!')
        print('=======original')
        print(nums)
        print('=======sort_func')
        print(sort_func(nums))
        print()
        print('=======right answer')
        print(sorted(nums))
