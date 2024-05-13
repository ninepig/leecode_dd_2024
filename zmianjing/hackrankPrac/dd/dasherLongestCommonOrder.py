## followup 不存在dp每个节点里的方法
## https://takeuforward.org/data-structure/print-longest-common-subsequence-dp-26/
## https://www.geeksforgeeks.org/printing-longest-common-subsequence/

class Solution:
    def longestCommonOrderPath(self, res1, res2):
        ## sanitty check
        if not res1 or not res2:
            return []
        leng1 = len(res1)
        leng2 = len(res2)
        dp = [[[] for _ in range(leng1 + 1)] for _ in range(leng2 + 1)]

        for i in range(1, leng1 + 1):
            for j in range(1, leng2 + 1):
                if res2[j - 1] == res1[i - 1]:  ## if we have same target:
                    dp[i][j].extend(dp[i - 1][j - 1])
                    dp[i][j].append(res1[i - 1])
                else:
                    ## we get a longer one
                    if len(dp[i][j - 1]) < len(dp[i - 1][j]):
                        dp[i][j].extend(dp[i - 1][j])
                    else:
                        dp[i][j].extend(dp[i][j - 1])

        print(dp[-1][-1])
        return dp[-1][-1]


sol = Solution()
sol.longestCommonOrderPath(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
                           ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"])

