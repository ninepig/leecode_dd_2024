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
            target_counter = collections.Counter(target)
            difference = self.compareDifference(target_counter, candidate)
            print(difference)
            ## need ask if k or mins k
            if difference <= k:
                res.append(candidate)

        return res

    def compareDifference(self, target_counter, candidate):
        diff = 0
        for char in candidate:
            if target_counter[char] > 0:
                target_counter[char] -= 1
            else:
                diff += 1
        return diff


orignal_name = "five guys"
target_list = ["five ugsy", "fiee guys", "eivf guys"]
target_list_k = ["five kkkk", "fiee guys", "eivf kkys"]
sol = Solution()
print(sol.nameWithOneSwap(target_list, orignal_name))
print(sol.nameWithkdiff(target_list_k, orignal_name, 2))