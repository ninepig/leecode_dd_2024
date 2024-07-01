import collections


class Solution:
    def nameWithOneSwap(self, names, target):
        ## santity check
        if not names or len(names) == 0 or not target:
            raise Exception("invalid input")
        target_counter = collections.Counter(target)
        res = []
        for item in names:
            cur_counter = collections.Counter(item)
            if target_counter != cur_counter:
                continue
            ## char is good, check if we can find target with 1 swap
            diff_count = 0
            for i in range(len(target)):
                if target[i] != item[i]:
                    diff_count += 1
                if diff_count > 2:
                    break
            if diff_count == 2 or diff_count == 0:
                res.append(item)

        return res

    def nameWithkdiff(self, names, target, k):
        if not names or len(names) == 0 or not target:
            raise Exception("invalid input")
        res = []
        for candidate in names:
            difference = self.compareDifference(target, candidate)
            print(difference)
            ## need ask if k or mins k
            if difference <= k:
                res.append(candidate)

        return res

    # def compareDifference(self, target_counter, candidate):
    #     diff = 0
    #     for char in candidate:
    #         if target_counter[char] > 0:
    #             target_counter[char] -= 1
    #         else:
    #             diff += 1
    #     return diff

    ## 这个才是正确的方法 最终版本
    def compareDifference(self, target, candidate):
        # memo = collections.defaultdict(int)
        # for char in candidate:
        #     memo[char] += 1
        # for char in target_counter:
        #     if memo[char]:
        #         memo[char] -=1
        # return sum(memo.values())
        scount = collections.Counter(candidate)
        tcount = collections.Counter(target)
        count = 0
        for ch in scount:
            count += max(scount[ch] - tcount[ch], 0)  # We only add positive differences
        for ch in tcount:
            count += max(tcount[ch] - scount[ch], 0)  # We only add positive differences
        return count // 2

orignal_name = "five guys"
target_list = ["five ugsy", "fiee guys", "eivf guys"]
target_list_k = ["five kkkk", "fiee guys", "eivf kkys"]
sol = Solution()
print(sol.nameWithOneSwap(target_list, orignal_name))
print(sol.nameWithkdiff(target_list_k, orignal_name, 2))