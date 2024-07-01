'''撞小行星题'''
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            ## 这个flag 很重要
            cur_exist = True
            while stack and stack[-1] > 0 > asteroid  and cur_exist : ## collision happen
                if stack[-1] < abs(asteroid):
                    ## top one explode
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    cur_exist = False ## both explode
                else:
                    cur_exist = False # only curr one explode

            if cur_exist : ## this aseroid not destroyed
                stack.append(asteroid)

        return stack

    ## Followup：如果相同size不explode而是change direction怎么处理，比如8 -8变成-8 8
    # 先处理duplcated的， 把顺序改变 然后 再类似第一题的处理， 只不过相同的就要加入
    def asteroidCollisionFollowup(self, asteroids: List[int]) -> List[int]:

        stack = []
        # first check duplciated value and changed that
        for i in range(len(asteroids) - 1):
            if abs(asteroids[i]) == abs(asteroids[i+1]):
                asteroids[i] *= -1
                asteroids[i + 1] *= -1

        for asteroid in asteroids:
            ## 这个flag 很重要
            cur_exist = True
            while stack and stack[-1] > 0 > asteroid and cur_exist:  ## collision happen
                if stack[-1] < abs(asteroid):
                    ## top one explode
                    stack.pop()
                # if that is eqaul , we just push to stack
                elif stack[-1] == abs(asteroid):
                    stack.append(asteroid)
                    cur_exist = False  ## current one insert to queue
                else:
                    cur_exist = False  # only curr one explode

            if cur_exist:  ## this aseroid not destroyed
                stack.append(asteroid)

        return stack

test = Solution()
case = [3,8,8,-8]
print(test.asteroidCollisionFollowup(case))