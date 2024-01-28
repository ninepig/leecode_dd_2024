class Solution:
    '''
    mem + dfs
    '''
    def tribonacci(self, n: int) -> int:
        mem = [0 for _ in range(n+1)]
        return self.memdp(n,mem)

    def memdp(self, n, mem):
        if n == 0 :
            return 0
        if n == 1 or n == 2:
            return 1
        if mem[n] != 0:
            return mem[n]

        mem[n] = self.memdp(n-2,mem) + self.memdp(n-1,mem) + self.memdp(n-3,mem)

        return mem[n]

