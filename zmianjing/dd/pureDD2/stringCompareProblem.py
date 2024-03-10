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


## check this out
## https://www.1point3acres.com/bbs/thread-1048134-1-1.html

class Solution:
    def findSimilarNameWithOneChange(self,resName:str, candidates:list[str])->list[str]:
        ## can change at most once , means we can have 2 char different,  and counter should be same
        res_counter = collections.Counter(resName)
        res = []
        for candidate in candidates: # naming conversion is not good
            counter = 0
            candidate_counter = collections.Counter(candidate)
            if candidate_counter != res_counter:
                continue
            for i in range(len(resName)):
                if resName[i] != candidate[i]:
                    counter += 1
                if counter >2 : # 注意事项，提前break 的条件
                    break
            if counter ==0 or counter == 2:
                res.append(candidate)

        return res

    # k difference
    def findSimilarNameWithKdiff(self,orignal:str, candidates:list[str],k:int)->list[str]:
        # k difference, we compare with dict
        res = []
        orignal_dict = collections.defaultdict(int)
        for char in orignal:
            orignal_dict[char] += 1

        for candidate in candidates:
            candidate_dict = collections.defaultdict(int)
            for char in candidate:
                candidate_dict[char] += 1
            diff = self.helper(orignal_dict,candidate_dict)
            if diff <= k :
               res.append(candidate)

        return res

    # def helper(self, orignal_dict, candidate_dict):
    #     diff = 0
    #     for key,value in orignal_dict.items():
    #         if key not in candidate_dict:
    #             diff += value
    #         else:
    #             diff += abs(value - candidate_dict[key])
    #
    #     return diff

    def helper(self, name_dict, candidate_dict):
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
print(test.findSimilarNameWithKdiff(orignal,k_lists,2))



