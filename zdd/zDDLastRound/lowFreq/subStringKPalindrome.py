'''
https://chatgpt.com/c/a46db54a-ec28-4784-b3df-f6c5c63df4f6

要解决这个问题，我们可以使用动态规划（Dynamic Programming）来计算将字符串分割成k个回文子串的方法数。这个问题涉及两个关键部分：

判断某个子串是否是回文。
使用动态规划计算将字符串分割成k个回文子串的方法数。
具体步骤如下：

判断子串是否是回文：我们可以使用一个二维数组isPalindrome，其中isPalindrome[i][j]表示从索引i到索引j的子串是否是回文。
这个数组可以通过动态规划在O(n^2)时间内预处理完成。

动态规划求解：使用一个二维数组dp，其中dp[i][j]表示将前i个字符分成j个回文子串的方法数
。我们从前向后遍历字符串，对于每个字符尝试将其作为最后一个子串的结束位置，并根据之前的状态更新当前状态。

感觉不对。。
'''
import collections

'''
这个算法的时间复杂度是O(n^3)，其中n是字符串的长度。
'''
def countPalindromicPartitions(s: str, k: int) -> int:
    n = len(s)

    # Step 1: Precompute whether s[i:j+1] is a palindrome
    isPalindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        isPalindrome[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    isPalindrome[i][j] = True
                else:
                    isPalindrome[i][j] = isPalindrome[i + 1][j - 1]

    # Step 2: Use dynamic programming to count the ways to partition the string
    '''
    使用一个二维数组dp，其中dp[i][j]表示将前i个字符分成j个回文子串的方法数。
    我们从前向后遍历字符串，对于每个字符尝试将其作为最后一个子串的结束位置，并根据之前的状态更新当前状态
    '''
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: there's 1 way to partition an empty string into 0 parts

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(i):
                '''
                对于每个位置i，尝试将从位置l到i-1的子串作为最后一个回文子串，如果它是回文，则更新dp[i][j]
                j-1 代表着 k减少了1位 因为 l -- i -1 满足palindrome 所以k减少1位 可以达到
                transfer：
                if s[l][size] palindrom
                dp[size][k] += dp[l][k-1] 
                '''
                if isPalindrome[l][i - 1]:
                    dp[i][j] += dp[l][j - 1]

    return dp[n][k]


# Example usage
s = "aabb"
k = 3
print(countPalindromicPartitions(s, k))  # Output: 1


'''
第一道题目是给一个string 和数字k，要求return int 有多少种能将string分成k substrings，
并且每一个substring都是palindrome的方法。我用的backtracking，但感觉是不是可以用dp之类的优化。
'''






