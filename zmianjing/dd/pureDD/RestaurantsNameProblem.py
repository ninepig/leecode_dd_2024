'''
第一道题是给一个Restaurant name (String)和一个List of Restaurant names(String)，找出所有名字相似的restaurant
相似的Restaurant是指最多只能交换一次character, e.g.
Input:
Restaurant Name: "five guys"
Restaurant Name List: ["five ugsy", "fiee guys", "eivf guys"]
Output:
[ "eivf guys"]
"eivf guys" -> swap e and f -> "five guys"
("five ugsy" is not because it need 2 swaps, and "fiee guys" is not because it can not swap)
第二道题是第一题的followup，给一个Restaurant name (String)和一个List of Restaurant names(String)，找出可以经过K次变化变成restaurant的anargam
anargam 是指原字母的任意组合，比如"Five guys" -> "guys five", "five ugsy", "eivf guys“。。。都是anagram
K次变化是指可以更改K个character
Input:
Restaurant Name: "five guys"
Restaurant Name List: ["five kkkk", "fiee guys", "eivf kkys"]
K: 2
Output:
["fiee guys", "eivf kkys"]
"fiee guys" -> change e to v -> "five guys", "five guys" is an anagram
"eivf kkys" -> change k, k to i and g -> "eivf guys", "eivf guys" is an anagram
'''
# 第一题是 1790 , 用map的方法做 最暴力,
import collections

from LinkedList import List


class solution:
    def findSimilarRestaunt(self,orignal:str,targets):
        orignalCounter = collections.Counter(orignal)
        res = []
        for target in targets:
            targetCounter = collections.Counter(target)
            count = 0
            if orignalCounter != targetCounter:
                continue ## we have different chars , so return false
            for i in range(len(orignal)):
                if orignal[i] != target[i]:
                    count += 1
                if count > 2:
                    break
            if count == 0 or count == 2:
                res.append(target)

        return res
    # 第二题有歧义, 必须问清楚, k anagram 是不是最多有个k个字符不同的angram
    def findKanagramRestaunt(self,orignal:str,targets, k : int):
        # orignalCounter = collections.defaultdict()
        orignalCounter = dict()
        for char in orignal:
            if char in orignalCounter:
                orignalCounter[char] += 1
            else:
                orignalCounter[char] = 1
        res = []
        for target in targets:
            # targetCounter = collections.defaultdict()
            targetCounter = dict()
            for char in target:
                if char in targetCounter:
                    targetCounter[char] += 1
                else:
                    targetCounter[char] = 1

            diff = self.helper(orignalCounter,targetCounter)
            if diff <= k:
                res.append(target)
        return res

    def helper(self, orignalCounter, targetCounter):
        diff = 0
        for item in orignalCounter.items():
            key,value = item[0],item[1]
            if key not in targetCounter:
                diff += value
            else:
                diff += abs(value - targetCounter[key])

        return diff

if __name__ == '__main__':
    # lists =   ["five ugsy", "fiee guys", "eivf guys"]
    k_lists = ["five kkkk", "fiee guys", "eivf kkys"]
    orignal = "five guys"
    test = solution()
    print(test.findKanagramRestaunt(orignal,k_lists,2))

    # orignalCounter = collections.defaultdict()
    # for char in orignal:
    # #     if char not in orignalCounter:
    # #         orignalCounter[char] = 1
    # #     else:
    #     orignalCounter[char] += 1

    # orignalCounter = collections.defaultdict(int)
    # python的写法问题
    # for char in orignal:
    #     orignalCounter[char] += 1


    # orignalCounter = dict()
    # # python的写法问题
    # for char in orignal:
    #     if char not in orignalCounter:
    #         orignalCounter[char] = 1
    #     else:
    #         orignalCounter[char] += 1
    #
    # # print(orignalCounter)
    # print(orignalCounter)