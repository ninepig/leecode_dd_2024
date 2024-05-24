class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        l = (intLength + 1) // 2   # 可以唯一确定回文数的前半部分的长度
        ## 起始数
        start = 10 ** (l - 1) - 1   # start + k 即为第 k 个 l 位无前导零整数
        ## 上届
        limit = 10 ** l - 1   # l 位无前导零整数的上界
        res = []
        # 将前半部分恢复为对应的回文数
        def recover(num: int) -> int:
            if intLength % 2 == 0:
                return int(str(num) + str(num)[::-1])
            else:
                return int(str(num)[:-1] + str(num)[::-1])

        # 依次处理询问
        for query in queries:
            if start + query > limit:
                # 不存在
                res.append(-1)
                continue
            res.append(recover(start + query))
        return res

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/find-palindrome-with-fixed-length/solutions/1379240/zhao-dao-zhi-ding-chang-du-de-hui-wen-sh-6i6j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。