import collections


class Solution:
    def minWindow76(self, s1: str, s2: str) -> str:
        need = collections.defaultdict()
        windows = collections.defaultdict()
        size = len(s1) + 1# max size will be s1's size
        left , right = 0, 0
        start = 0
        valid = 0

        for c in s2:
            need[c] += 1

        while right < len(s1):
            right_char = s1[right]
            if right_char in need:
                windows[right_char] += 1
                if windows[right_char] == need[right_char]:
                    valid += 1

            ## we found matching subsequence in string s1
            ## shrink windows
            while valid == len(need):
                # found target
                if right - left + 1 < size:
                    start = left
                    size = min(size, right - left + 1)
                left_char = s1[left]
                if left_char in need:
                    windows[left_char] -= 1
                    if windows[left_char] != need[left]:
                        valid -= 1
                left += 1
            right += 1

        if size == len(s1) + 1:  # does not exist
            return ''

        return s1[start: start + size]
        # new left = right

##题目没写清楚, 这个要求相对顺序保持一致 , 所以不能用hashtable来做 要用纯纯的双指针(劈叉) + sliding windows
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
                # 从右向左找到左侧窗口
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