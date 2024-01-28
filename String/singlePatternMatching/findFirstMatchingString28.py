class Solution:
    '''最经典的单模式匹配题'''
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        size_hay = len(haystack)
        size_needle = len(needle)
        while i < size_hay and j < size_needle:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                # 回退长度, j 是已经比较过字符串的长度 , +1 是进位 (bf匹配的原则)
                i = i - j + 1
                j = 0

        # 全部比较完成
        if j == size_needle:
            return i - j

        else:
            return -1 