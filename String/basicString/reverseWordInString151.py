class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

'''
标准的以及非标准的（python库）'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        cur = ""
        for ch in s:
            if ch == ' ':
                if cur:
                    words.append(cur)
                    cur = ""
            else:
                cur += ch

        if cur:
            words.append(cur)

        for i in range(len(words) // 2):
            words[i], words[len(words) - 1 - i] = words[len(words) - 1 - i], words[i]

        return " ".join(words)