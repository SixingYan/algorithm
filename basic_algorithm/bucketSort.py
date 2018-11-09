"""
如果已经知道输入的序列的最大值是M，则建立M个桶，每次往桶里加入即可
时间复杂度 M+N
"""


def bucketSort(nums, M):
    buckets = {}
    for i in range(M):
        buckets[i] = 0
    for n in nums:
        buckets[n] += 1

    result = []
    for i in range(M):
        for j in range(buckets[i]):
            result.append(i)
    return result
