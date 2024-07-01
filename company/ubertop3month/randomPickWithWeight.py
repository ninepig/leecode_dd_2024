class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.prefix_sum = [0] * n
        self.prefix_sum[0] = w[0]

        # 前缀和
        for i in range(1, n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]
        print(self.prefix_sum)


    def pickIndex(self) -> int:
        seed = random.randint(1, self.prefix_sum[-1])
        index = bisect_left(self.prefix_sum, seed)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# 作者：程序员赤小豆
# 链接：https://leetcode.cn/problems/random-pick-with-weight/solutions/967614/chi-xiao-dou-nojie-ti-python-dai-ni-du-d-7iev/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。