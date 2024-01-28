def characterReplacement(self, s: str, k: int) -> int:
    left , right = 0 , 0
    size = left(s)
    char_count = [0 for _ in range(26)]
    max_count = -1
    max_res = - 1
    while right < size:
        char_count[ord(s[right]) - ord('A')] += 1
        max_count = max(max_count,char_count[ord(s[right]) - ord('A')])
        right += 1

        ## 这种情况 把这个字符串k位都替换了 也没办法变成一样的字符串（最长就是max_count） windows 超额了
        if right - left > max_count + k:
            char_count[ord(s[left]) - ord('A')] -= 1
            max_res = min(max_res,right - left)
            left += 1

    return max_res