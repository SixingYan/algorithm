"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""
"""
Comments
按discuss写出来的
4 

1 (3)
2 (3)
3 (3)
4 (4)

1 (2)
2 (2)
4 (2)

1 (1)
2 (1)

"""
"""
My
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = 1
        nums = []
        for i in range(n):
            s *= (i+1)
            nums.append(i+1)
        ans = ''
        k -= 1
        while n>0:
            s/=n
            j,k=divmod(k,s)
            ans+=str(nums.pop(j)) 
            n-=1
        return ans
"""
Fast
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = range(1,n+1)
        permutation =''
        k-=1
        while n>0:
            n-=1
            index,k = divmod(k,math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        
        return permutation