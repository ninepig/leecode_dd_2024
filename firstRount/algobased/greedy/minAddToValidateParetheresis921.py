class Solution:
    '''
    基本贪心
    为了最终添加的最少括号数，我们应该尽可能将当前能够匹配的括号先进行配对。则剩余的未完成配对的括号数量就是答案。
    遍历字符串，判断当前字符。
如果当前字符为左括号 (，则令 left_cnt 加 1。
如果当前字符为右括号 )，则令 left_cnt 减 1。如果 left_cnt 减到 -1，说明当前有右括号不能完成匹配，则答案数量 res 加 1，并令 left_cnt 重新赋值为 0。
遍历完之后，令 res 加上剩余不匹配的 left_cnt 数量。
最后输出 res。
    '''
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left_count = 0
        for char in s:
            if char == '(':
                left_count += 1
            elif char == ')':
                left_count -= 1
                if left_count == -1:
                    res += 1
                    left_count = 0

        return res + left_count

