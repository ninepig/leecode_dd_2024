class Solution:
    def starCollision(self, stars: list[int]):
        ## sanity check
        if not stars or len(stars) == 0:
            raise Exception("wrong input")

        stack = []
        for star in stars:
            cur_exists = True
            while stack and stack[-1] > 0 > star and cur_exists:
                if abs(stack[-1]) > abs(star):  ## current star explode
                    cur_exists = False
                elif abs(stack[-1]) == abs(star):  ## both explode
                    stack.pop(-1)
                    cur_exists = False
                else:  ## top one explode
                    stack.pop(-1)

            ## if cur star not explode , we push to stack
            if cur_exists:
                stack.append(star)

        return stack

    def starCollisionFollowup(self, stars: list[int]):
        ## sanity check
        if not stars or len(stars) == 0:
            raise Exception("wrong input")

        ## we handle same value item by changing their direction from end to begin.
        ## then we do same as question 1

        stack = []
        for i in range(len(stars) - 2, -1, -1):
            if abs(stars[i + 1]) == abs(stars[i]):
                stars[i + 1] *= -1
                ## bug here, in hack rank , variable will be blue
                stars[i] *= -1
        for star in stars:
            cur_exists = True
            while stack and stack[-1] > 0 > star and cur_exists:
                if abs(stack[-1]) > abs(star):  ## current star explode
                    cur_exists = False
                elif abs(stack[-1]) == abs(star):  ## we don't do any thing , just push star to stack
                    stack.append(star)
                    cur_exists = False  ## still set this false to avoid duplciate push
                else:  ## top one explode
                    stack.pop(-1)
            ## if cur star not explode , we push to stack
            if cur_exists:
                stack.append(star)

        return stack


case = [3, 8, 8, -8]
sol = Solution()
print(sol.starCollisionFollowup(case))