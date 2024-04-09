class Solution:
    '''
    1 using stack
    2 potive heading to right , negative heading to right
    3 so collision happen when first asteroid potive and second one negative
        1 abs value bigger one stay
        2 same value both expolde

    '''
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for star in asteroids:
            cur_star = True # flag to judge if this star will explode
            # top of stack is positive and cur is negitave
            while stack and stack[-1] > 0 > star and cur_star:
                if abs(stack[-1]) > abs(star):
                    cur_star = False # cur one explode
                elif abs(stack[-1]) == abs(star):
                    cur_star = False
                    stack.pop(-1) ## both explode
                else:
                    stack.pop(-1) ## only stack one explode

            ## stop loop, no more explode for this star
            if cur_star :
                stack.append(star)

        return stack

    ## Followup：如果相同size不explode而是change direction怎么处理，比如8 -8变成-8 8
    ## 3，8，8，-8结果变成-8 8 8
    ## 因为变了方向 所以 原来向右的会向左 就会出现 3 8 8 -8 如果第二个向左了。 那就会把3炸了
    ## 所以这道题最好的做法 就是从后往前 先看有没有重复的node 如果有重复的node 先把他自身的方向转换了 再重新按照第一部来做 这样能保证碰撞

    def asteroidCollisionDupChangeDirection(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(len(asteroids) - 2 , -1 , -1):
            if abs(asteroids[i]) == abs(asteroids[i+1]):
                asteroids[i+1] = asteroids[i+1] * -1
                asteroids[i] = asteroids[i] * -1
        for star in asteroids:
            cur_exist = True
            while stack and stack[-1] > 0 > star and cur_exist :
                if abs(stack[-1]) > abs(star) :
                    cur_exist = False
                elif abs(stack[-1]) < abs(star):
                    stack.pop(-1)
                else: ## we could have couple star for loop
                    stack.append(star)
                    cur_exist = False
            if cur_exist :
                stack.append(star)
        return stack

if __name__ == '__main__':
    case = [3,8,8,-8]
    sol = Solution()
    print(sol.asteroidCollisionDupChangeDirection(case))



