## https://leetcode.com/problems/string-compression/description/

def compress(self, chars: List[str]) -> int:
    chars += " "  # use a dummy char to take care last char
    start = 0
    compress_end = 0
    for i in range(len(chars)):
        if chars[i] != chars[start]:  # only take action when new char starts
            chars[compress_end] = chars[start]
            compress_end += 1
            count = i - start
            if count > 1:
                for k in str(count):
                    chars[compress_end] = k
                    compress_end += 1
            start = i
    return compress_end