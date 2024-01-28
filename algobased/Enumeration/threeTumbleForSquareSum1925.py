from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        # if n <=0 :
        #     return 0
        # count = 0
        # for i  in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1 , n):
        #             if k*k == i*i + j*j:
        #                 count += 1
        # 枚举复杂了
    
        cnt = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int(sqrt(a * a + b * b + 1))
                if c <= n and a * a + b * b == c * c:
                    cnt += 1
        return cnt
