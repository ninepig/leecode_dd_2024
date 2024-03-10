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
import collections


class Solution:
    ## 最多换一次。 所以要么 difference 是0 要么是 2 ， 如果是1 肯定就有问题， 因为无法swap
    def findSimilarNameWithOneChange(self,resName:str, candidates:list[str])->list[str]:
        name_counter = collections.Counter(resName)
        res = []
        for candidate in candidates:
            diff = 0
            candidate_counter = collections.Counter(candidate)
            if candidate_counter != name_counter:
                continue
            for i in range(len(resName)):
                if resName[i] != candidate[i]:
                    diff += 1
                if diff > 2: ## missing this step, can boost up
                    break
            if diff == 0 or diff == 2:
               res.append(candidate)

        return res

    ## max k difference , so diff < k means that is candidate

    def findSimilarNameWithKdifference(self,resName:str, candidates:list[str],k:int)->list[str]:
        name_dict = collections.defaultdict(int)
        res = []
        for c in resName:
            name_dict[c] += 1

        for candidate in candidates:
            if len(candidate) != len(resName):continue
            candidate_dict = collections.defaultdict(int)
            for char in candidate:
                candidate_dict[char] += 1
            diff = self.compareDiff(name_dict,candidate_dict)
            if diff <= k: ## at least k change
            # if diff == k ## k change
                res.append(candidate)

        return res


    ## good one
    def compareDiff(self, name_dict, candidate_dict):
        counter = 0
        for char in name_dict:
            if char in candidate_dict:
                counter += abs(name_dict[char] - candidate_dict[char]) ## 相同字符出现次数之差
            else:
                counter +=  name_dict[char] ## 不存在字符储量

        ## 因为这个是算anagram ，所以目标是字符出现次数一样
        return counter



test = Solution()
k_lists = ["five kkkk", "fiee guys", "eivf kkys"]
orignal = "five guys"
print(test.findSimilarNameWithKdifference(orignal,k_lists,2))