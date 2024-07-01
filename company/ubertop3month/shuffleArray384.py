## https://algo.itcharge.cn/Solutions/0300-0399/shuffle-an-array/#%E6%80%9D%E8%B7%AF-1-%E6%B4%97%E7%89%8C%E7%AE%97%E6%B3%95
## 纯数学
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        self.shuffle_nums = self.nums.copy()
        for i in range(len(self.shuffle_nums)):
            swap_index = random.randrange(i, len(self.shuffle_nums))
            self.shuffle_nums[i], self.shuffle_nums[swap_index] = self.shuffle_nums[swap_index], self.shuffle_nums[i]
        return self.shuffle_nums
