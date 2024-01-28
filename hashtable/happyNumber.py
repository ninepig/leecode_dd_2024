class Solution:
    '''经典小题'''
    def getNext(self, n: int):
        res = 0
        while n > 0 :
            n,digit = divmod(n,10)
            res += digit**2
        return res


    def isHappy(self, n: int) -> bool:
        h_set = set()
        while n > 0 and n not in h_set:
            h_set.add(n)
            n = self.getNext(n)

        return n == 1