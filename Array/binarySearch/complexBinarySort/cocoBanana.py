class Solution:
    '''
    二分法的高级应用
    一定要把问题模型化。 找到最低值 最高值。 对于这个题 最高就是猩猩吃香蕉的速度


    先来看 k 的取值范围，因为 k 是整数，且速度肯定不能为 0 吧，为 0 的话就永远吃不完了。所以k 的最小值可以取 1。k 的最大值根香蕉中最大堆的香蕉个数有关，因为 1 个小时内只能选择一堆吃，不能再吃其他堆的香蕉，则 k 的最大值取香蕉堆的最大值即可。即 k 的最大值为 max(piles)。

我们的目标是求出 h 小时内吃掉所有香蕉的最小速度 k。现在有了区间「[1, max(piles)]」，有了目标「最小速度 k」。接下来使用二分查找算法来查找「最小速度 k」。至于计算 h 小时内能否以 k 的速度吃完香蕉，我们可以再写一个方法 canEat 用于判断。如果能吃完就返回 True，不能吃完则返回 False。下面说一下算法的具体步骤。

使用两个指针 left、right。令 left 指向 1，right 指向 max(piles)。代表待查找区间为 [left, right]

取两个节点中心位置 mid，判断是否能在 h 小时内以 k 的速度吃完香蕉。

如果不能吃完，则将区间 [left, mid] 排除掉，继续在区间 [mid + 1, right] 中查找。
如果能吃完，说明 k 还可以继续减小，则继续在区间 [left, mid] 中查找。
当 left == right 时跳出循环，返回 left。
    '''
    def canEat(self, piles, hour, speed):
        time = 0
        for pile in piles:
            # 除非能被整除，如果剩下1个香蕉 也需要额外的1个小时, get ceiling of pile / speed
            time += (pile + speed - 1) // speed
        return time <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canEat(piles, h, mid):
                left = mid + 1
            else:
                right = mid

        return left