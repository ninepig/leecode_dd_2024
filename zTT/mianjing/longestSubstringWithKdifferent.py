class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for i in range(1,27):  # 枚举窗口内字符种类的数量
            # 剪枝：如果字符种类数量 * 每个字符最少出现的次数 > 字符串长度，后面就不需要再枚举了
            if i * k > len(s):
                break
            # 开始正常的滑窗
            left = 0
            cnt = Counter()
            for right, x in enumerate(s):
                cnt[x] += 1
                while len(cnt) > i:  # 当窗口内的字符种类数大于枚举的字符种类数时，不符合条件了
                    y = s[left]
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        del cnt[y]
                    left += 1
                if len(cnt) == i: # 符合窗口内的字符数条件
                    if all(x >= k for x in cnt.values()):  # 符合每个字符>=k的条件
                        ans = max(ans,right-left+1) # 更新答案
        return ans
#
# 作者：小姜可
# 链接：https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/solutions/2560525/gu-ding-chuang-kou-nei-zi-fu-chong-lei-s-jr27/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_cnt = {s[0]: 1}
        res = 1
        left = right = 0
        while right + 1 < len(s):
            right += 1
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1
            while len(char_cnt) > 2:
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    char_cnt.pop(s[left])
                left += 1

            res = max(res, right - left + 1)
