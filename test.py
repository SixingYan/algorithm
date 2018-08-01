
class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        s, z, l, sIdx, zIdx, lInx = self.countNum(nums)

        if s == 0 and z == 0:     # only larger
            value = self.arrProduct(nums)

        elif s == 0 and l == 0:   # only zero
            value = 0

        elif s > 0 and l == 0:
            if z > 0:           # smaller and zero
                parts = self.seperateArr(z, zIdx, nums)
                value = self.maxProductNoTarget(parts, True, productSmaller)

            else:               # only smaller
                value = self.productSmaller(nums)

        elif s > 0 and l > 0:                  # smaller and larger
            parts = self.seperateArr(s, sIdx, nums)
            value = self.maxProductNoTarget(parts, False)

        elif l > 0 and s > 0:                  # larger and zero
            parts = self.seperateArr(s, sIdx, nums)
            value = self.maxProductNoTarget(parts, True)

        else:                   # smaler zero larger
            if s % 2 == 0:
                value = self.arrProduct(nums)
            else:
                parts = self.seperateArr(z, zIdx, nums)
                value = self.maxProductNoTarget(parts, True)

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
        s, z, l = (0, 0, 0)
        sIdx = []
        zIdx = []
        lInx = []
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

    def maxProductNoTarget(self, numsList, isZero, product_func):
        maxVList = []

        for nums in numsList:

            if isZero is True:
                value = product_func([n for n in nums if n != 0])
                if value < 0:
                    value = 0
            else:
                value = product_func([n for n in nums if n > 0])
            maxVList.append(value)

        return max(maxVList)

    def arrProduct(self, nums):
        total = 1

        for i in range(0, len(nums)):
            total *= nums[i]

        return total

    def productSmaller(self, nums):
        if len(nums)%2 == 0:
            return self.arrProduct(nums)
            
        a = self.arrProduct(nums[1:])
        b = self.arrProduct(nums[0:-1])
        if a > b:
            return a
        else:
            return b

if __name__ == '__main__':
    nums = [-2,0,-1]
    a = Solution()
    result = a.maxProduct(nums)
    print(result)
