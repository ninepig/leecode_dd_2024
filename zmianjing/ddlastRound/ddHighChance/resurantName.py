
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


class solution:
    ## SAWP ONCE
    def findSimilarRestaunt(self,orignal:str,targets:list[str])->list[str]:
        if not orignal or not targets or len(targets) == 0:
            return []
        orignal_counter = collections.Counter(orignal)
        N = len(orignal)
        res = []
        for target in targets:
            swap_counter = 0
            target_counter = collections.Counter(target)
            ## if counter does not match
            if orignal_counter != target_counter:
                continue
            for i in range(N):
                if orignal[i] != target[i]:
                    swap_counter += 1
                if swap_counter > 2:
                    break
            if swap_counter == 0 or swap_counter == 2:
               res.append(target)

        return res

    def findSimilarRestauntWithKDiffs(self, orignal: str, targets: list[str],k:int) -> list[str]:

        if not orignal or len(orignal) == 0 or not targets :
            return []
        ## form dict
        orignal_dict = dict()
        target_dict = dict()
        res = []
        for c in orignal:
            if c not in orignal_dict:
                orignal_dict[c] = 1
            else:
                orignal_dict[c] += 1
        for target in targets:
            if len(target) != len(orignal) : continue
            target_dict.clear()
            for c in target:
                if c not in target_dict:
                    target_dict[c] = 1
                else:
                    target_dict[c] += 1

            difference = self.getDiff(target_dict,orignal_dict)
            if difference == k:
                res.append(target)

        return res

    def getDiff(self, target_dict, orignal_dict):
        diff = 0
        for k,v in orignal_dict.items():
            if k not in target_dict:
                diff += v
            else:
                diff += abs(target_dict[k] - v)

        return diff

if __name__ == "__main__":
    orignal_name = "five guys"
    target_list =  ["five kkkk", "fiee guys", "eivf kkys"]
    sol = solution()
    print(sol.findSimilarRestaunt(orignal_name,target_list))
    print(sol.findSimilarRestauntWithKDiffs(orignal_name,target_list,2))