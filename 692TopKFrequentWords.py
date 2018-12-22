"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
"""
Comments
"""
"""
My
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wDict = {}
        for w in words:
            if w in wDict.keys():
                wDict[w] += 1
            else:
                wDict[w] = 1
        # freq 顺序
        fDict = {}
        for w in wDict.keys():
            f = wDict[w]
            if f not in fDict.keys():
                fDict[f] = [w]
            else:
                fDict[f].append(w)
        # 字母顺序      
        for f in fDict.keys():
            fDict[f].sort()
        # 同字母之间，取数量最小的
        sList = []
        for ar in sorted(list(fDict.items()), reverse=True, key=lambda w:w[0]):
            sList.extend(ar[1]) 
        return [sList[i] for i in range(k)]
"""
Fast
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        a_dict = {}
        #words = sorted(words,reverse=True)
        for word in words:
            if word not in a_dict:
                a_dict[word] = 1
            else:
                a_dict[word] += 1
        a_dict = sorted(a_dict.items(),key=lambda e:e[0])
        a_list = sorted(a_dict,key=lambda e:e[1],reverse=True)
        res = []
        for key,val in a_list:
            if k>0:
                res.append(key)
                k -= 1
        return res