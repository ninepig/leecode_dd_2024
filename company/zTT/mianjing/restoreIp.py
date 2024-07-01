class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(idx, n, cur):
            if len(cur) > 4:
                return
            if idx == n:
                if len(cur) == 4:
                    ans.append('.'.join(cur))
            else:
                for i in range(idx, n):
                    t = 0
                    for j in range(idx, i + 1):
                        t = t * 10 + (ord(s[j]) - ord('0'))
                    # 首ip为0的情况 就不用考虑后面了，只可能是0 ，也就是不能是xxx.012.xx 这种ip
                    if s[idx] == '0' and i != idx:
                        break
                    if t > 255:
                        break
                    cur.append(str(t))
                    dfs(i + 1, n, cur)
                    cur.pop()
        dfs(0, len(s), [])
        return ans

# 作者：宫水三叶
# 链接：https://leetcode.cn/problems/restore-ip-addresses/solutions/2519711/gong-shui-san-xie-hui-su-suan-fa-yun-yon-khnj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 作者：Daz2ling DriscollSzv
# 链接：https://leetcode.cn/problems/restore-ip-addresses/solutions/2772894/ling-shen-ke-hou-ti-hui-su-suan-fa-tao-l-teje/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。