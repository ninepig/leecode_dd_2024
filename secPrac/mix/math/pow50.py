class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n== 0:
            return 1
        if n < 0 :
            return self.myPow(1/x,-n)
        res = 1
        ## 这个来模拟.
        while n:
            if n % 2:
                res *= x
                n -= 1
            else:
                x *= x
                n = n // 2

        return res


# First part
# 递归清晰一点
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n)  # 1
        else:
            return 1 / self.helper(x, -n)  # 2


    def helper(self, x, n):
        if n == 0:  # 3
            return 1

        temp = self.myPow(x, n // 2)  # 4

        if int(n % 2) == 0:  # 5
            return temp * temp
        else:
            return temp * temp * x  # 6