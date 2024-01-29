class Solution:

    '''i knows j return True
        not, return False
    '''
    def knows(self,i: int, j: int) -> bool:
        pass

    # 请你实现：返回「名人」的编号

    # 1brutal force way
    # 非常直接 n^2 时间
    def findCelebrity(self,n: int) -> int:
        candidate = 0
        for i in range(n):
            other = 0 # inital target from 0
            while other < n :
                if candidate == other:
                    other += 1
                    continue
                # if some one know candidate, or candidate know some one , candidate is wrong
                if self.knows(candidate,other) or not self.knows(other,candidate):
                    break
                other += 1
                if other == n: # reach to end
                    return candidate
        return -1

    def findCelebrity(self,n: int) -> int:
        # 先假设 cand 是名人
        candidate = 0
        for other in range(1,n):
            ## once there is invalide candidate, we use other to replace him
            if not self.knows(other,candidate) or self.knows(candidate,other):
                candidate = other
        # verify if that is a good candidate
        for i in range(n):
            if candidate == i:
                continue
            if self.knows(candidate,i) or not self.knows(i,candidate):
                return -1
        return candidate
