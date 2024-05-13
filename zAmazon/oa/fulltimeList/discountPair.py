# https://www.fastprep.io/problems/get-discount-pairs
## 这个有点复杂。。换个方法做
class Solution:
    def getDiscountPairs(self, x: int, prices: list[int]) -> int:
        count = 0
        remainder_counts = [0] * x

        # Count the number of products with each remainder when divided by x
        for price in prices:
            remainder = price % x
            remainder_counts[remainder] += 1

        # Count the number of pairs whose sum is divisible by x
        for i in range(1, x // 2 + 1):
            if i == x - i:
                count += remainder_counts[i] * (remainder_counts[i] - 1) // 2
            else:
                count += remainder_counts[i] * remainder_counts[x - i]

        # Count the number of pairs whose sum is divisible by x and both products have remainder 0
        count += remainder_counts[0] * (remainder_counts[0] - 1) // 2

        return count
