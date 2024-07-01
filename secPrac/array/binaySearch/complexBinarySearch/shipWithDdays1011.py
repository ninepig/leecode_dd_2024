from firstRount.LinkedList import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # need 为需要运送的天数
            # cur 为当前这一天已经运送的包裹重量之和
            # 不能拆分包裹 这点没注意.
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight

            if need <= days:
                right = mid
            else:
                left = mid + 1

        return left


作者：力扣官方题解
链接：https: // leetcode.cn / problems / capacity - to - ship - packages - within - d - days / solutions / 743995 / zai - d - tian - nei - song - da - bao - guo - de - neng - l - ntml /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。