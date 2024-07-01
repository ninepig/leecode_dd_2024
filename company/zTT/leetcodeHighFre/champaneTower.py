## 数学模拟题
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(1, query_row + 1):
            nextRow = [0] * (i + 1)
            for j, volume in enumerate(row):
                if volume > 1:
                    nextRow[j] += (volume - 1) / 2
                    nextRow[j + 1] += (volume - 1) / 2
            row = nextRow
        return min(1, row[query_glass])

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/champagne-tower/solutions/1979893/xiang-bin-ta-by-leetcode-solution-y87c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。