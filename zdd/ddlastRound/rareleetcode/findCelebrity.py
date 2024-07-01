'''

'''
class Solution:
    def findCelebrity(self,n:int)->int:
        candidate = 0
        ## find candidate
        for i in range(n):
            if self.knows(candidate,i): ## if candidate konw some one, that is not candidate
                candidate = i

        ## verify candidate
        for i in range(n):
            if candidate != i:
                if self.knows(candidate,i) or not self.knows(i,candidate):
                    return -1

        return candidate

    # def findCelebrity(self, n: int) -> int:
    #     # Initialize the candidate for celebrity to 0
    #     candidate = 0
    #     # Iterate over the range from 1 to n-1
    #     for i in range(1, n):
    #         # If the candidate knows person i, then switch candidate to i
    #         if knows(candidate, i):
    #             candidate = i
    #
    #     # Verify candidate is indeed a celebrity
    #     for i in range(n):
    #         # Make sure we skip comparing the candidate with themselves
    #         if candidate != i:
    #             # Candidate should not know anyone, and everyone should know the candidate
    #             if knows(candidate, i) or not knows(i, candidate):
    #                 # If the condition fails, return -1 because there is no celebrity
    #                 return -1
    #
    #     # If all checks pass, return the candidate as the celebrity
    #     return candidate

    def knows(self,candidate:int,other:int)->bool:
        pass


    def findCelebrityBrutalForce(self,n:int)->int:
        if n <= 1 :
            return -1
        ## brutal force way
        for i in range(1,n+1):
            candidate = i
            other = 1
            while other < n + 1:
                if other == candidate:
                    continue
                if self.knows(candidate,other) or not self.knows(other,candidate):
                    break
                if other == n : #loop end
                    return candidate
                other += 1
        return -1
