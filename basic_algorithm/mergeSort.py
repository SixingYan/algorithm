"""
分成两半
每次取两部分最小的填入临时数组，直到一部分先填完
把另一部分的剩余部分直接填进临时数组
再把临时数组里的数值回填到原始数组中
"""
from typing import List


def merge(nums: List, temArr: List, LPosIdx: int, RPosIdx: int, REndIdx: int)->List:
    LEndIdx = RPosIdx - 1
    pos = LPosIdx
    n = REndIdx - LPosIdx + 1

    # 这里是取等号
    while LPosIdx <= LEndIdx and RPosIdx <= REndIdx:
        if nums[LPosIdx] < nums[RPosIdx]:
            temArr[pos] = nums[LPosIdx]
            LPosIdx += 1
        else:
            temArr[pos] = nums[RPosIdx]
            RPosIdx += 1
        pos += 1

    while LPosIdx < LEndIdx:
        temArr[pos] = nums[LPosIdx]
        LPosIdx += 1
        pos += 1

    while RPosIdx < REndIdx:
        temArr[pos] = nums[RPosIdx]
        RPosIdx += 1
        pos += 1

    # copy back
    for i in range(REndIdx, REndIdx - n - 1, -1):
        nums[i] = temArr[i]

    return nums


def mergeSort(nums: List, temArr: List, startIdx: int, endIdx: int)->List:
    if startIdx < endIdx:
        center = int((startIdx + endIdx) / 2)
        nums = mergeSort(nums, temArr, startIdx, center)
        nums = mergeSort(nums, temArr, center + 1, endIdx)
        nums = merge(nums, temArr, startIdx, center + 1, endIdx)
    return nums


def main(nums: List)->List:
    temArr = [None for i in range(len(nums))]
    nums = mergeSort(nums, temArr, 0, len(nums) - 1)
    return nums

if __name__ == '__main__':
    main()
