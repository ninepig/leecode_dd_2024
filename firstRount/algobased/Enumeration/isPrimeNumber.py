class Solution:
    ## 如何计算质数, 看他能不能被自己的平方根整除, 基本的数学方法
    def isPrime(self, x):
        for i in range(2, int(pow(x, 0.5)) + 1):
            if x % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        cnt = 0
        for x in range(2, n):
            if self.isPrime(x):
                cnt += 1
        return cnt

    '''
    Create a list of booleans is_prime of length n, initialized to True.

Mark is_prime[0] and is_prime[1] as False since 0 and 1 are not prime.

Iterate from i = 2 to i * i < n:
a. If is_prime[i] is True, then iterate from j = i * i to j < n, marking is_prime[j] as False since j is a multiple of i.

Count the number of True values in is_prime.
'''
    def countPrimesGoodway(self, n: int) -> int:
        if n <= 2:
            return 0

        # Step 1
        is_prime = [True] * n

        # Step 2
        is_prime[0] = is_prime[1] = False

        # Step 3
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Step 4
        return sum(is_prime)

    def countPrimesGoodwayPac(self, n: int) -> int:
        if n < 2:
            return n
        is_prime = [True for _ in range(n)]
        # 0, 1 is prime
        is_prime[0] = False
        is_prime[1] = False

        # 从2 到 n的平方根
        for i in range(2,n**0.5+1):
            if is_prime[i]:
                # 如果i 是质数,他的乘积 肯定不是质数
                for j in range(i*i,n,i):
                    is_prime[j] = False

        return sum(is_prime)