class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        a = Counter(s).most_common()  # 按出现次数从大到小排序
        m = a[0][1]
        if m > n - m + 1:
            return ""

        ans = [''] * n
        i = 0
        for ch, cnt in a:
            for _ in range(cnt):
                ans[i] = ch
                i += 2
                if i >= n:
                    i = 1  # 从奇数下标开始填
        return ''.join(ans)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/reorganize-string/solutions/2779462/tan-xin-gou-zao-pai-xu-bu-pai-xu-liang-c-h9jg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。