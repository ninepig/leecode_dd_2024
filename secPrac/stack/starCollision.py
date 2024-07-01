class Solution:
    '''
    用栈来做的模拟题。
    如果是负数， 且栈顶不为空 我们要检查是否爆炸。
    如果是正数/负数栈顶为空 直接入栈
    '''
    def starCollision(self, stars: list[int]):
        if not stars or len(stars) == 0 :
            return []
        stack = []
        for star in stars:
            cur_exists = True
            while stack and stack[-1] > 0 > star and cur_exists:
                if abs(stack[-1]) > abs(star): ## current explode
                    cur_exists = False
                elif abs(stack[-1]) == abs(star): ## both explode
                    stack.pop(-1)
                    cur_exists = False
                else:##
                    stack.pop(-1)

            if cur_exists:
                stack.append(star)

        return stack

    def starCollision2(self,stars:list[int]):
        if not stars or len(stars) == 0 :
            return []
        stack = []
        ## preprocessing, revert star value from end first
        for i in range(len(stars) - 2 , -1 ,-1):
            if abs(stars[i]) == abs(stars[i+1]):
                stars[i] = stars[i] * -1
                stars[i + 1] = stars[i + 1] * -1

        for star in stars:
            cur_exist = True
            while stack and stack[-1] > 0 > star and cur_exist:
                if abs(stack[-1]) > abs(star): ## star exploded
                    cur_exist = False
                elif abs(stack[-1]) < abs(star):
                    stack.pop(-1)
                else:
                    stack.append(star)
                    cur_exist = False
            if cur_exist :
                stack.append(star)

        return stack

case = [3,8,8,-8]
sol = Solution()
print(sol.starCollision(case))
# print(sol.starCollision2(case))

