import functools

## 这道题不仅是排序题，更是python 语法题。 非常经典
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(nums_s)))
