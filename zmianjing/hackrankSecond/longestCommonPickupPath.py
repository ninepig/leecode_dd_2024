## https://www.geeksforgeeks.org/printing-longest-common-subsequence/
class Solution:
    def longestCommonOrderPath(self, res1, res2):
        if not res1 or not res2:
            return ""
        m = len(res1)
        n = len(res2)
        dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if res1[i - 1] == res2[j - 1]:
                    dp[i][j].extend(dp[i - 1][j - 1])
                    dp[i][j].append(res1[i - 1])
                else:
                    if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                        dp[i][j].extend(dp[i][j - 1])
                    else:
                        dp[i][j].extend(dp[i - 1][j])

        print(dp[-1][-1])
        return dp[-1][-1]

    def longestCommonOrderPathSaveSpace(self, res1, res2):
        if not res1 or not res2:
            return ""
        m = len(res1)
        n = len(res2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if res1[i - 1] == res2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = m
        j = n
        res = []
        while i > 0 and j > 0:
            if res1[i - 1] == res2[j - 1]:
                res.append(res1[i - 1])
                i -= 1
                j -= 1
            ## if value is not same, we find larger 's direction
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        res = res[::-1]
        print(res)


sol = Solution()
sol.longestCommonOrderPath(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
                           ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"])
sol.longestCommonOrderPathSaveSpace(
    ["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
    ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"])
