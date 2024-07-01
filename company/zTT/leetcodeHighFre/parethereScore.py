class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for c in s:
            if c == '(':
                stk.append(0)
            else:
                cur = stk.pop()
                stk.append(stk.pop() + max(cur * 2, 1))
        return stk[-1]

# 作者：宫水三叶
# 链接：https://leetcode.cn/problems/score-of-parentheses/solutions/1878233/by-ac_oier-0mhz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。