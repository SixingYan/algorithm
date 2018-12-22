"""
O(log2n)
"""


def binarySearch(nums, k) -> int:
    l = 0
    r = len(nums)
    while l < r:
        mid = int((l + r) / 2)
        if nums[mid] < k:
            l = mid + 1
        elif nums[mid] > k:
            r = mid - 1
        else:
            return nums[mid]
    return -1
