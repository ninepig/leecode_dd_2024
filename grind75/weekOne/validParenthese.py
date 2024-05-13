'''
基本的stack的应用
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return False
        stack = []
        for c in s :
            if c in "([{":
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] != '(':
                    return False
                stack.pop()
            elif c == "]":
                if stack and stack[-1] != '[':
                    return False
                stack.pop()
            elif c == "}":
                if stack and stack[-1] != '{':
                    return False
                stack.pop()

        return len(stack) == 0
