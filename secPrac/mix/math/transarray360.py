class Solution:
    def calFormula(self, x, a, b, c):
        return a * x * x + b * x + c

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        size = len(nums)
        res = [0 for _ in range(size)]

        # 直线
        if a == 0:
            if b >= 0:
                index = 0
                for i in range(size):
                    res[index] = self.calFormula(nums[i], a, b, c)
                    index += 1
            else:
                index = 0
                for i in range(size - 1, -1, -1):
                    res[index] = self.calFormula(nums[i], a, b, c)
                    index += 1
        else:
            # 二次函数, 波谷/波峰 横坐标
            diad = -(b / (2.0 * a))
            left, right = 0, size - 1

            if a > 0:
                index = size - 1
                while left < right:
                    if abs(diad - nums[left]) > abs(diad - nums[right]):
                        res[index] = self.calFormula(nums[left], a, b, c)
                        left += 1
                    else:
                        res[index] = self.calFormula(nums[right], a, b, c)
                        right -= 1
                    index -= 1
                res[index] = self.calFormula(nums[left], a, b, c)
            else:
                diad = -(b / (2.0 * a))
                left, right = 0, size - 1
                index = 0
                while left < right:
                    if abs(diad - nums[left]) > abs(diad - nums[right]):
                        res[index] = self.calFormula(nums[left], a, b, c)
                        left += 1
                    else:
                        res[index] = self.calFormula(nums[right], a, b, c)
                        right -= 1
                    index += 1
                res[index] = self.calFormula(nums[left], a, b, c)
        return res