class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not  candidates or len(candidates) == 0 :
            return []
        res = []
        path = []
        def backtrack(total,index):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(index , len(candidates)):
                if total + candidates[i] > target:
                    break

                total += candidates[i]
                path.append(candidates[i])
                backtrack(total,i) # 注意这里是i ，因为要根据当前位进行backtrack wenjing
                path.pop()
                total -= candidates[i]
        candidates.sort() ## wenjing 这个很重要， sort以后可以增加效率, 同时是为了      if total + candidates[i] > target: 可以work
        backtrack(0,0)
        return res

    # 去重 只能使用一次，所以需要去重，以及增加index判断
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not  candidates or len(candidates) == 0 :
            return []
        res = []
        path = []
        def backtrack(total,index):
            if total > target:
                return
            if total == target:
                res.append(path[:])
            for i in range(index ,len(candidates)):
                if total + candidates[i] > target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                total += candidates[i]
                path.append(candidates[i])
                backtrack(total,i)
                path.pop()
                total -=candidates[i]

        candidates.sort()
        backtrack(0,0)
        return res

class SolutionRight:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(total, start_index):
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                if total + candidates[i] > target:
                    break

                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i)
                total -= candidates[i]
                path.pop()

        candidates.sort()
        backtrack(0, 0)
        return res

