class Solution:
    # complexDs ---> 去重
    # 顺序输出 + 最小--> 单调栈
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        char_dict = dict()
        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        for c in s : # each c will count once
            if c not in stack: # in right order and removed depulcated
                # only pop top when we still have char  to make sure we can do in right order
                while stack and c < stack[-1] and c in char_dict and char_dict[c] > 0 : # we still have c in dict, which means we can pop that and build monotonic stack
                    stack.pop()
                stack.append(c)
            char_dict[c] -= 1

        return "".join(stack)