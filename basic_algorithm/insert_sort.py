""""""
from typing import List


def sort(nums: List[int]):
	for i in range(1, len(nums)):
        tmp = nums[i]
        j = i
        while j > 0 and tmp < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = tmp
    return nums
