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
                    diff_count +=1
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
        scount = collections.Counter(name)
        tcount = collections.Counter(target)
        count = 0
        for ch in scount:
            count += max(scount[ch] - tcount[ch], 0)  # We only add positive differences
        for ch in tcount:
            count += max(tcount[ch] - scount[ch], 0)  # We only add positive differences
        return count // 2