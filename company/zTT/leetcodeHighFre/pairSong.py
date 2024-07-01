class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        cnt = [0] * 60
        for t in time:
            # 先查询 cnt，再更新 cnt，因为题目要求 i<j
            # 如果先更新，再查询，就把 i=j 的情况也考虑进去了
            ans += cnt[(60 - t % 60) % 60]
            cnt[t % 60] += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2259343/liang-shu-zhi-he-de-ben-zhi-shi-shi-yao-bd0r1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。