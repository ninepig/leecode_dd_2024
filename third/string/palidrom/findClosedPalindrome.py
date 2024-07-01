# https://leetcode.cn/problems/find-the-closest-palindrome/solutions/1300885/xun-zhao-zui-jin-de-hui-wen-shu-by-leetc-biyt
'''
最高频。。也太难了。。纯模拟题
99321 --- 99399 ---》 99299
12399---》 12321 --》 12421
123333--> 123321 --> 回文数构造
如果进位了 或者退位了
99xxx999
1000001 需要作为备选

这个题就是把各种最近的回文数都构造出来 然后加入候选
用原数的前半部分替换后半部分得到的回文整数。
用原数的前半部分加一后的结果替换后半部分得到的回文整数。
用原数的前半部分减一后的结果替换后半部分得到的回文整数

'''

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        print(candidates)
        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)


test = "12345"
sol = Solution()
print(sol.nearestPalindromic(test))