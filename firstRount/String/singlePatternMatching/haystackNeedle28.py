class Solution:
    # brutal force 值得细品
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        length_i = len(haystack)
        length_j = len(needle)
        while i < length_i and j < length_j:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - (j - 1) # if not match, move i to i + removed j
                j = 0
        if j == length_j:
            return i - j
        else:
            return -1

    '''
    对于给定的文本串 T 与模式串 p，求出文本串 T 的长度为 n，模式串 p 的长度为 m。
通过滚动哈希算法求出模式串 p 的哈希值 hash_p。
再通过滚动哈希算法对文本串 T 中 n - m + 1 个子串分别求哈希值 hash_t。
然后逐个与模式串的哈希值比较大小。
如果当前子串的哈希值 hash_t 与模式串的哈希值 hash_p 不同，则说明两者不匹配，则继续向后匹配。
如果当前子串的哈希值 hash_t 与模式串的哈希值 hash_p 相等，则验证当前子串和模式串的每个字符是否真的相等（避免哈希冲突）。
如果当前子串和模式串的每个字符相等，则说明当前子串和模式串匹配。
如果当前子串和模式串的每个字符不相等，则说明两者不匹配，继续向后匹配。
比较到末尾，如果仍未成功匹配，则说明文本串 T 中不包含模式串 p，方法返回 -1
'''
    def strStrRk(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        hash_2 = hash(needle)
        for i in range(len1 - len2 + 1):
            hash_1 = hash(haystack[i:i+len2])
            if hash_1 != hash_2 :
                continue

            k = 0
            # compare char 1 by1 to avoid hash collision
            for j in range(len2):
                if haystack[i + j] != needle[j]:
                    break
                k += 1
            if k == len2:
                return i
        return -1