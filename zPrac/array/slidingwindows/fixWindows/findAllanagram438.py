import collections

'''经典的滑动窗口
这题的关键是
valid 这个计数器 必须要和need的size一样大
统计的有效的字符数量'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0 , 0
        need = collections.defaultdict()
        for ch in p:
            need[ch] += 1

        windows = collections.defaultdict()
        windows_size = len(p)
        valid_count = 0
        res = []
        while right < len(s):
            if s[right] in need:
                windows[s[right]] += 1
                if windows[s[right]] == need[s[right]]:
                       valid_count += 1

            if right - left + 1 >= windows_size:
                if valid_count == len(need): # 有效字母数量一样 所以比价windows的长度
                    res.append(left)
                # shrink windows
                if s[left] in need:
                    windows[s[left]] -= 1
                    if windows[s[left]] == need[s[left]]:
                        valid_count -= 1
                left += 1
            right += 1

        return res

