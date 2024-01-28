'''
转换成
windows size 最多为 2 ， 至多2种字符、数字 的最长子数组 求长度
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = dict()
        window_size = 2
        ans = 0
        left, right = 0, 0
        while right < len(fruits):
            if fruits[right] in window:
                window[fruits[right]] += 1
            else:
                window[fruits[right]] = 1

            while len(window) > window_size:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans