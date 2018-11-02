"""
“向前比较”

从1开始循环
游标先指向要比较的目标
如果目标小于前面的一个数，
	将前面的数复制到游标所在位置，
	游标前移（此时已有两个一样的数）
如果游标不小于前面的数，
	该位置就是目标应该插入的位置
开始下一个循环
"""
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