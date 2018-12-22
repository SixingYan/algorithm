"""
https://blog.csdn.net/MoreWindows/article/details/6684558
1．i =L; j = R; 将基准数挖出形成第一个坑a[i]。

2．j--由后向前找比它小的数，找到后挖出此数填前一个坑a[i]中。

3．i++由前向后找比它大的数，找到后也挖出此数填到前一个坑a[j]中。

4．再重复执行2，3二步，直到i==j，将基准数填入a[i]中。
"""
def quickSort(nums, l, r):
	if l < r:
		i = l
		j = r
		x = nums[l]

		while i < j:
			while i < j and s[j] <= x:
				j -= 1
			if i < j:
				s[i] = s[j]
				i += 1
			while i < j and s[i] > x:
				i += 1
			if i < j:
				s[j] = s[i]
				j -= 1
		nums[i] = x
		nums = quickSort(nums, l, i-1)
		nums = quickSort(nums, i+1, r)
	return nums

