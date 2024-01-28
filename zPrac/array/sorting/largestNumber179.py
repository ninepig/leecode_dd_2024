# 贪心 + cmp_to_key 自定义规则

import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1 # 大于1 排在后面, 加上reverse 就可以完成 , 贪心 x + y > y + x , y就排在前面 对于两两数组
            else:
                return -1
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(nums_s)))