class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ## corner case s ,  t
        s_final = self.getFinalString(s)
        print("s_final",s_final)
        t_final = self.getFinalString(t)
        print("t_final",t_final)
        return s_final == t_final

    def getFinalString(self, s:str,) -> str:
        stack = []
        for c in s:
            if c == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)


        return "".join(stack)


test = Solution()
s = "ab#cd"
t = "acd"

print(test.backspaceCompare(s,t))
