import collections


class Solution:
    def nameWithOneSwap(self, names, target):
        if not names or len(names) == 0 :
            return []
        res = []
        target_coutner = collections.Counter(target)
        for name in names:
            name_counter = collections.Counter(target)
            if target_coutner != name_counter:
                continue ## char is not matching, which indicated invalid
            diff_count = 0
            for i in range(len(target)):
                if target[i] != name[i]:
                    diff_count += 1
                if diff_count >2 :
                    break # ealry stop
            if diff_count == 0 or diff_count == 2:
               res.append(name)
        return res

    def nameWithKdiff(self,names,target,k):
        if not names or len(names) == 0 :
            return []
        res = []
        for name in names:
            if len(name) != len(target) : continue
            diff = self.getDiff(name,target)
            if diff <= k:
                res.append(name)

        return res

    ##最优解法
    def getDiff(self, name, target):
        # get freq of each characters
        original_count = collections.Counter(name)
        target_count = collections.Counter(target)
        count = 0
        ## 或者用26个字符 全部走一遍 用abs
        '''
            for i in range(26): if we using char array
            count += abs(original_count[i] - target_count[i])
        '''

        for ch in original_count:
            count += max(original_count[ch] - target_count[ch], 0)  # We only add positive differences
        for ch in target_count:
            count += max(target_count[ch] - original_count[ch], 0)  # We only add positive differences
        return count // 2


test = Solution()
# swap_lists = ["five ugsy", "fiee guys", "eivf guys"]
k_lists = ["five kkkk", "fiee guys", "eivf kkys"]

orignal = "five guys"
# print(test.nameWithOneSwap(swap_lists,orignal))
print(test.nameWithKdiff(k_lists,orignal,3))