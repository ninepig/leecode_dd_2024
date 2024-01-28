class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ## upper case or lower case?
        s.lower()
        vowels = ['a','e','i','o','u']
        left = 0
        right = 0
        res = 0
        windows_count = 0
        while right < len(s):
            if s[right] in vowels:
                windows_count += 1

            if right - left + 1 >= k:
                ## 计数
                res = max(res,windows_count)
                # 只有left 在windows之中 再去除left
                if s[left] in vowels:
                    windows_count -= 1
                # 无论如何left都是+=1
                left += 1
            right += 1

        return res
