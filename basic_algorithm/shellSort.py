"""
把hk, hk+1, hk+2, ..., N-1中的每个位置i，依次放入i-hk, i-2*hk, ..., 中的正确位置上
相当于做一趟插入排序 
"""


def shellSort(nums):
    h = int(len(nums) / 2)
    while h > 0:
        for i in range(h, len(nums)):
            tmp = nums[i]
            for j in range(i, 0, -h):
                if tmp < nums[j - h]:
                    nums[j] = nums[j - h]
            nums[j] = tmp
        h = int(h / 2)
    return nums
