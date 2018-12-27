"""
这个写法是从大到小排序
比最小的子节点都要小
为什么插入是只用一半的数据？
	堆的定义是节点应小于它的两个子节点，而子节点通过2n和2n+1计算，所以根节点最多从n/2开始
	所以保证有子节点的节点（从n/2到0）满足以上条件即可
中间的步骤类似于插入排序
	给定一个节点的值，把这个值向下寻找应该插入的位置
建立堆 O(n)
重新排序 O(nlogn)
就地排序 O(1)
"""


def leftChild(i):
    return 2 * i + 1


def perDown(nums, i, n):

    tmp = nums[i]
    while leftChild(i) < n:
        child = leftChild(i)

        # choose the greater from two childs
        if child != n - 1 and nums[child] < nums[child + 1]:
            child += 1

        if tmp < nums[child]:
            nums[i] = nums[child]
        else:
            break

        # turn to the child node
        i = child

    nums[i] = tmp

    return nums


def heapSort(nums):
    for i in range(int(len(nums) / 2), -1, -1):
        nums = perDown(nums, i, len(nums))  # 从中间开始，取全范围的数据进行排序

    for i in range(len(nums) - 1, 0, -1):
        tmp = nums[0]  # 取出根节点（这是最小的数）
        nums = perDown(nums, 0, i)  # 从根节点（0）开始，删掉根节点并重排剩下的，每次缩小范围
        nums[i] = tmp  # 把这个数值放入最后一个位置

    return nums
