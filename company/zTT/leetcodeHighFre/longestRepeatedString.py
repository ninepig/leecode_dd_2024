'''
Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

二分法

'''

class Solution:
    def search(self, S: str, length: int) -> bool:
        visited = set()
        for i in range(len(S) - length + 1):
            substring = S[i:i + length]
            if substring in visited: return True
            visited.add(substring)
        return False

    def longestRepeatingSubstring(self, S: str) -> str:
        left, right = 0, len(S) - 1
        while left <= right:
            middle = left + (right - left + 1) // 2
            if self.search(S, middle):
                left = middle + 1
            else:
                right = middle - 1
        return left - 1