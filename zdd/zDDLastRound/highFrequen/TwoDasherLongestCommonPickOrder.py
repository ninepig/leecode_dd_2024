'''
# Two Dashers can complete up to N possible ordered pickups on a certain day. These pickups are represented by two arrays of length N, one for each dasher.
#
# A pickup is represented by the name of the merchant, for example, "chilis" or "mcdonalds".
#
# We could have the following two arrays that represent the pickup jobs for the two dashers:
#
# dasher1_pickups:["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"]
# dasher2_pickups:["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]
#
# The two dashers ride in the same car and want to complete the same pickup jobs together while respecting the original ordering.
# At the same time however, they want to complete as many deliveries as possible to maximize their payout.
# Question: What is the longest sequence of pickups that these two dashers can complete together?
'''

'''
这道题是longest common subsequnce 的变形题

'''

## 利用dp里记录数组来做

def longestCommonPickUpOrder(s1,s2):
    if not s1 or not s2:
        return ""
    length_s1 = len(s1)
    length_s2 = len(s2)
    dp = [[[] for _ in range(length_s2 + 1)] for _ in range(length_s1 + 1) ]
    for i in range(1,length_s1 + 1):
        for j in range(1,length_s2 + 1):
            if s1[i - 1] == s2[j - 1]: ## if we met same target, extend previous string, add current one
                dp[i][j].extend(dp[i-1][j-1])
                dp[i][j].append(s1[i-1])
            else: ## if not same target, we get previous longer distance
                if len(dp[i][j-1]) > len(dp[i-1][j]):
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


## 先算出长度，倒推法
def longestCommonPickUpOrderReverse(s1,s2):
    if not s1 or not s2:
        return ""
    length_s1 = len(s1)
    length_s2 = len(s2)
    dp = [[0 for _ in range(length_s2 + 1)] for _ in range(length_s1 + 1) ]
    for i in range(1,length_s1 + 1):
        for j in range(1,length_s2 + 1):
            if s1[i - 1] == s2[j - 1]: ## if we met same target, extend previous string, add current one
                dp[i][j] = 1 + dp[i-1][j-1]
            else: ## if not same target, we get previous longer distance
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    final_length = dp[-1][-1]
    print(final_length)
    i = length_s1
    j = length_s2

    res = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]: ## if we have same value
           res.append(s1[i-1])
           # index
           i -= 1
           j -= 1
        elif dp[i-1][j] > dp[i][j-1]: ## we go with direction larger one
            i -= 1
        else:
            j -= 1

    return res[::-1]


print(longestCommonPickUpOrder(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
          ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]))


print(longestCommonPickUpOrderReverse(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
          ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]))

