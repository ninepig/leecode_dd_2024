'''要仔细想想的windows题

向右扩大窗口，匹配字符，直到匹配完 s2 的最后一个字符。
当满足条件时，缩小窗口，并更新最小窗口的起始位置和最短长度。
缩小窗口到不满足条件为止。
这道题的难点在于第二步中如何缩小窗口。当匹配到一个子序列时，可以采用逆向匹配的方式，从 s2 的最后一位字符匹配到 s2 的第一位字符。找到符合要求的最大下标，即是窗口的左边界。

整个算法的解题步骤如下：

使用两个指针 left、right 代表窗口的边界，一开始都指向 0 。min_len 用来记录最小子序列的长度。i、j 作为索引，用于遍历字符串 s1 和 s2，一开始都为 0。
遍历字符串 s1 的每一个字符，如果 s1[i] == s2[j]，则说明 s2 中第 j 个字符匹配了，向右移动 j，即 j += 1，然后继续匹配。
如果 j == len(s2)，则说明 s2 中所有字符都匹配了。
此时确定了窗口的右边界 right = i，并令 j 指向 s2 最后一个字符位置。
从右至左逆向匹配字符串，找到窗口的左边界。
判断当前窗口长度和窗口的最短长度，并更新最小窗口的起始位置和最短长度。
令 j = 0，重新继续匹配 s2。
向右移动 i，继续匹配。
遍历完输出窗口的最短长度（需要判断是否有解）。
'''

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        i, j = 0, 0
        min_len = float('inf')
        left, right = 0, 0
        while i < len(s1):
            if s1[i] == s2[j]:
                j += 1
            # 完成了匹配
            if j == len(s2):
                right = i
                j -= 1
                while j >= 0:
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1
                if right - i + 1 < min_len:
                    left = i
                    min_len = right - left + 1
                j = 0
            i += 1
        if min_len != float('inf'):
            return s1[left: left + min_len]
        return ""