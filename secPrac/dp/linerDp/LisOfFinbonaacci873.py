class Solution:
    def lenLongestFibSubseqBF(self, arr: List[int]) -> int:
        # 暴力法
        res = 0
        size = len(arr)
        for i in range(size):
            for j in range(i + 1 ,size):
                temp_size = 0
                temp_i = i
                temp_j = j
                k = j + 1
                while k < size:
                    if arr[k] == arr[temp_j] + arr[temp_i]:
                        temp_size += 1
                        temp_i = temp_j
                        temp_j = k
                    k += 1
                    res = max(res,temp_size)

        if res > 0:
            return res + 2 # at least we have 2 for fibonacci
        else:
            return 0

    def lenLongestFibSubseqHashmap(self, arr: List[int]) -> int:
        value_idx = dict()
        size = len(arr)
        ans = 0
        for idx,value in enumerate(arr):
            value_idx[value] = idx

        for i in range(size):
            for j in range(i + 1, size):
                temp_size = 0
                temp_i = i
                temp_j = j
                while (arr[temp_i] + arr[temp_j]) in value_idx:
                    temp_size += 1
                    temp = value_idx[arr[temp_i] + arr[temp_j]]
                    temp_i = temp_j
                    temp_j = temp
                    ans = max(ans,temp_size)

        if ans > 0:
            return ans + 2  # at least we have 2 for fibonacci
        else:
            return 0

    '''
    state: dp[i][j] 以 i， j 结尾 lis的值
    state[i][j] initial -- > dp[i][j] = 2 每一个值都是2 （j > i） ,因为至少有2个值
    state tansfer--> if k = i + j (value) ==> dp[j][k] = max(dp[j][k], dp[i][j] + 1)
    利用hashmap 减少计算
    '''
    def lenLongestFibSubseqDP(self, arr: List[int]) -> int:
        size = len(arr)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        ans = 0
        # inital
        for i in range(size):
            for j in range(i + 1 ,size):
                dp[i][j] = 2

        value_idx = dict()
        for idx,value in enumerate(arr):
            value_idx[value] = idx

        for i in range(size):
            for j in range(i + 1 ,size):
                if (arr[i] + arr[j]) in value_idx: # fibo exist
                    k = value_idx[arr[i] + arr[j]]
                    arr[j][k] = max((arr[i][j] + 1), arr[j][k])
                    ans = max(arr[j][k],ans)

        if ans > 2:
            return ans
        else:
            return 0
