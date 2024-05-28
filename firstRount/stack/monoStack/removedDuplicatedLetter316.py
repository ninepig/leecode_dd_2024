'''
因为要维护秩序，所以要用stack，同时字典序，所以用单调递减栈
去重 complexDs
非常好的题
第二次做的时候一定要看看有什么别的方法
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        letter_count = dict()
        for ch in s :
            if ch in letter_count:
                letter_count[ch] += 1
            else:
                letter_count[ch] = 1

        for ch in s:
            if ch not in stack:
                # 递减栈, 同时存在重复，同时比栈顶元素小
                while stack and ch < stack[-1] and stack[-1] in letter_count and letter_count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            letter_count[ch] -= 1

        return ''.join(stack)