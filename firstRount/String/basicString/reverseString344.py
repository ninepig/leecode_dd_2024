class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        left , right = 0, size - 1

        while left < right :
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        for item in str_list:
            size = len(item)
            left, right = 0, size - 1

            while left < right:
                item[left], item[right] = item[right], item[left]
                left += 1
                right -= 1

        return ' '.join(str_list)