'''
leetcode 316

1 去重---》hashmap
2 不打乱， 按顺序遍历。 利用栈 /或者数组
3 字典序最小。

结合三点---》利用单调栈 + dict的数据结构来做

'''
import collections


class Solution:

    ## 错误的
    def removeDuplicateLetters(self, s: str) -> str:
        if not s or len(s) == 0 : return s
        stack = []
        counter = collections.Counter(s)
        for i in range(len(s)):
            ## monotonic decreasing stack
            ## 我们要出栈是判断栈顶元素， 所以要在dict里查找栈顶元素是否可以被pop出去。
            while stack and stack[-1] > s[i] and stack[-1] in counter and counter[stack[-1]] > stack.pop():
            stack.append(s[i])
            counter[s[i]] -= 1 ## 入栈的时候就要在counter里减少1

        return "".join(stack)
    def removeDuplicateLettersRightOne(self, s: str) -> str:
        if not s or len(s) == 0 : return s
        stack = []
        letter_counts = collections.Counter(s)
        for ch in s:
            if ch not in stack: ##要加一条这个判断。。如果已经存在 就不放了。。
                while stack and ch < stack[-1] and stack[-1] in letter_counts and letter_counts[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            letter_counts[ch] -= 1

        return ''.join(stack)
