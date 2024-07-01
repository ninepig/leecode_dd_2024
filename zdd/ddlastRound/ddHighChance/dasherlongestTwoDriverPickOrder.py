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
#
# Note: The two dashers must complete the deliveries in the above order (from left to right) but are allowed to skip pickup jobs.
# IE, It is okay for the dashers to go from "walmart" to "mcdonalds" together, but they now forfeit the right to complete any delivery between those two merchants, or complete any delivery before their respective "walmarts".
#
# Example 1:
# dasher1_pickups:["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"]
# dasher2_pickups:["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]
# returns ["chilis", "walmart", "chilis", "burger king"]
#
# dasher1_pickups:["chilis", "albertsons", "mcdonalds"]
# dasher2_pickups:["burger king", "jamba juice", "applebees"]
# *Dasher1 and Dasher2 do not share any of the same pickup jobs, so they do not have any pickup jobs together.
# returns [].

# Based on LCS (https://leetcode.com/problems/longest-common-subsequence/);
# if it is a match extend it by the previous matched array. Instead of tracking the length, track the matched words.

def lcs(text1, text2):
    if not text1 or not text2:
        return ""
    s = len(text1)
    t = len(text2)
    dp = [[[] for _ in range(t + 1)] for _ in range(s + 1)]

    for i in range(1, s + 1):
        for j in range(1, t + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j].extend(dp[i - 1][j - 1])
                dp[i][j].append(text1[i - 1])

            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
    return dp[-1][-1]


print(lcs(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
          ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]))



print(lcs(["chilis", "albertsons", "mcdonalds"],
          ["burger king", "jamba juice", "applebees"]))



def lcs2(text1:str, text2:str):
    if not text1 or not text2 or len(text1) == 0 or len(text2) == 0:
        return []
    l1 = len(text1)
    l2 = len(text2)
    dp = [[[] for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1,l1 + 1):
        for j in range(1,l2 + 1):
            ## dp arrary start from 1, so text array start from i - 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j].extend(dp[i-1][j-1])
                dp[i][j].append(text1[i - 1])
            else:
                ## 不能用max 必须用 长度比较 这里是错的
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]


# print(lcs(["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"],
#           ["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]))


#
# print(lcs2(["chilis", "albertsons", "mcdonalds"],
#           ["burger king", "jamba juice", "applebees"]))