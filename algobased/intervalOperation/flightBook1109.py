from algobased.intervalOperation.carPooling1094 import diff


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    # nums 初始化为全 0
    nums = [0] * n
    # 构造差分解法
    df = diff(nums)

    for booking in bookings:
        # 注意转成数组索引要减一哦
        i = booking[0] - 1
        j = booking[1] - 1
        val = booking[2]
        # 对区间 nums[i..j] 增加 val
        df.increment(i, j, val)
    # 返回最终的结果数组
    return df.result()