class Solution:
    '''classic stack
    '''
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False

        return True

