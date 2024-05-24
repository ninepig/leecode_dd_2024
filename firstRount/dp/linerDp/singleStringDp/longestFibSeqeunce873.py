class Solution:
    def lenLongestFibSubseqHashmap(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        idx_map = dict()
        for idx,value in enumerate(arr):
            idx_map[value] = idx

        for i in range(size):
            for j in range(i+1,size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                while arr[temp_i] + arr[temp_j] in idx_map:
                    temp_ans += 1
                    k = idx_map[arr[temp_i] + arr[temp_j]]
                    temp_i = temp_j
                    temp_j = k

                    ans = max(temp_ans,ans)

        if ans > 0 :
            return ans + 2 # default we have at least length 2

        return ans


class Solution:
    def lenLongestFibSubseqHashmapDp(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        idx_map = dict()
        for idx,value in enumerate(arr):
            idx_map[value] = idx

        # state define --> dp[i][j] means 2 end number i,j 's longest fib number
        dp = [[0 for _ in range(size)] for _ in range(size)]

        # inital
        for i in range(size):
            for j in range(i+1,size):
                dp[i][j] = 2 # at least we have 2, no for dp[0][0]

        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] + arr[j] in idx_map: # means fib number exist
                    # dp transfer function
                    k = idx_map[arr[i] + arr[j]]
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)

                    ans = max(arr,dp[j][k])

        if ans > 2 :
            return ans
        return 0
