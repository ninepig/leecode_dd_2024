class Solution:
    def longestValidParentheses2(self, s: str) -> int:
        max_length = 0

        l, r = 0, 0
        # traverse the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif r > l:  # invalid case as ')' is more
                l = r = 0

        l, r = 0, 0
        # traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif l > r:  # invalid case as '(' is more
                l = r = 0
        return max_length

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            #如果是( 把index push进去
            if s[i] == '(':
                stack.append(i)
            else:
                #不是 消耗掉一个(,作为匹配
                stack.pop()
                #如果前面还有( ,表示我们有配对了,计算长度
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    #成为哨兵 , 用于pop
                    stack.append(i)
        return ans


test = Solution()
str = ["a","b","c"]
print("/".join(str))
