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
    def sameNameWithOneSwap(self,name:str,name_list:list[str]) -> list[str]:
        if not name or not name_list or len(name)==0 or len(name_list) == 0:
            return []
        name_counter = collections.Counter(name)
        res = []

        for target in name_list:
            target_counter = collections.Counter(target)
            diff = 0
            if target_counter != name_counter:
                continue
            for i in range(len(target)):
                if target[i] != name[i]:
                    diff += 1
                if diff > 2:
                    continue
            if diff ==0 or diff == 2:
                res.append(target)
        return res


    "angram 就是改变字符， 无论位置  需要确定这个"
    def sameNameWithKanagram(self,name:str,name_list:list[str],k:int) -> list[str]:
        if not name or not name_list or len(name) == 0 or len(name_list) == 0:
            return []
        name_dict = collections.defaultdict(int)
        for c in name_dict:
            name_dict[c] += 1

        res = []

        for target in name_list:
            if len(target)!= len(name): continue ## need confirm with interviewer "changing can be add and delete or not"
            target_dict =collections.defaultdict(int)
            for c in target:
                target_dict[c] += 1
            diff = self.find_counter_diff(self,target_dict,name_dict)
            if diff <= k:
                res.append(target)

        return res

    def find_counter_diff(self, self1, target_dict, name_dict):
        diff = 0
        ## 因为是angaram 所以我们只需要算name---》 target的char的diff 就可以。 target里的char是神恶魔不需要管。
        for c in name_dict:
            if c in target_dict:
                diff += abs(name_dict[c] - target_dict[c])
            else:
                diff += name_dict[c]

        return diff



test = solution()
swap_lists = ["five ugsy", "fiee guys", "eivf guys"]
# k_lists = ["five kkkk", "fiee guys", "eivf kkys"]

orignal = "five guys"
# print(test.sameNameWithOneSwap(orignal,swap_lists))
print(test.sameNameWithKanagram(orignal,swap_lists,2))


