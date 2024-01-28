'''
差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。

res = [0] * len(diff)
# 根据差分数组构造结果数组
res[0] = diff[0]
for i in range(1, len(diff)):
    res[i] = res[i - 1] + diff[i]

这样构造差分数组 diff，就可以快速进行区间增减的操作，如果你想对区间 nums[i..j] 的元素全部加 3，那么只需要让 diff[i] += 3，然后再让 diff[j+1] -= 3 即可
'''


# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

# 差分数组工具类
class Difference:
    # 差分数组
    def __init__(self, nums: List[int]):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        # 根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    # 给闭区间 [i, j] 增加 val（可以是负数）
    def increment(self, i: int, j: int, val: int) -> None:
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    # 返回结果数组
    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res


'''
1109 
'''
def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    # nums 初始化为全 0
    nums = [0] * n
    # 构造差分解法
    df = Difference(nums)

    for booking in bookings:
        # 注意转成数组索引要减一哦
        i = booking[0] - 1
        j = booking[1] - 1
        val = booking[2]
        # 对区间 nums[i..j] 增加 val
        df.increment(i, j, val)
    # 返回最终的结果数组
    return df.result()


# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。
'''
370'''
def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    # nums 初始化为全 0
    nums = [0] * length
    # 构造差分解法
    df = Difference(nums)

    for update in updates:
        i, j, val = update[0], update[1], update[2]
        df.increment(i, j, val)

    return df.result()


'''
1094
'''
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    # 最多有 1001 个车站
    nums = [0] * 1001
    # 构造差分解法
    df = Difference(nums)

    for trip in trips:
        # 乘客数量
        val = trip[0]
        # 第 trip[1] 站乘客上车
        i = trip[1]
        # 第 trip[2] 站乘客已经下车，
        # 即乘客在车上的区间是 [trip[1], trip[2] - 1]
        j = trip[2] - 1
        # 进行区间操作
        df.increment(i, j, val)

    res = df.result()

    # 客车自始至终都不应该超载
    for i in range(len(res)):
        if capacity < res[i]:
            return False
    return True