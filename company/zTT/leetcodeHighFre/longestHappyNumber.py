class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        num_map = {'a': a, 'b': b, 'c': c}
        res = ''
        while True:
            # 贪心法-动态获取当前剩余字符里面的最大与中间的使用 less, mid, most 三个字符会实时变化
            less, mid, most = sorted(num_map.keys(), key=lambda x: num_map[x])
            # print(less, mid, most)
            if (len(res) < 2 or not res[-2] == res[-1] == most) and num_map[most] > 0:
                res += most
                num_map[most] -= 1
            elif (not res[-2] == res[-1] == mid) and num_map[mid] > 0:
                res += mid
                num_map[mid] -= 1
            else:
                return res

# 作者：uint32
# 链接：https://leetcode.cn/problems/longest-happy-string/solutions/1249186/tan-xin-fa-si-lu-jian-dan-xing-neng-gao-im9td/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def addChars(queue, strs):
            val, char = heapq.heappop(queue)
            if not val or (len(strs) >= 2 and strs[-2] == strs[-1] == char and (not queue or not addChars(queue, strs))):
                return False
            strs.append(char)
            heapq.heappush(queue, (val + 1, char))
            return True

        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        ans = []
        while pq and addChars(pq, ans):
            pass
        return "".join(ans)

# 作者：Benhao
# 链接：https://leetcode.cn/problems/longest-happy-string/solutions/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。