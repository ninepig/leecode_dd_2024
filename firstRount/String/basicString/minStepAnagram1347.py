import collections

'''
默认的dict还不能做
    默认的要这么做
    sampleDict = {}
    test = "abc"
    for char in test:
        if char not in sampleDict:
            sampleDict[char] = 1
        else:
             sampleDict[char] += 1
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = collections.defaultdict(int)
        # python的写法问题
        for char in s:
            memo[char] += 1
        for char in t:
            if memo[char]:
                memo[char] -= 1
        return sum(memo.values())
