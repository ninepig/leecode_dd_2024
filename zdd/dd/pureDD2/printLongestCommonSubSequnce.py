
## https://www.geeksforgeeks.org/printing-longest-common-subsequence/
# https://www.1point3acres.com/bbs/thread-974556-1-1.html
## follow up --> 多个， 那就是记录下max 的length值， 然后在dp数组里找 这个max值对应的string ，然后开始往后回溯 找出所有的
## TODO
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    len_ = dp[n][m]
    i = n
    j = m

    index = len_ - 1
    str_ = ""
    for k in range(1, 1 + len_):
        str_ += "$"  # dummy string
        print(str_)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            str_ = s1[i - 1] + str_[:-1]
            print(str_)
            index -= 1
            i -= 1
            j -= 1
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif dp[i - 1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("The Longest Common Subsequence is", str_)


def main():
    s1 = "abcde"
    s2 = "bdgek"

    lcs(s1, s2)


if __name__ == "__main__":
    main()