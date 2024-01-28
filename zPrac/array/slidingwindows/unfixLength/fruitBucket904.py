'''
滑动窗口应用题
'''
class Solution:
    # 水果数量就是 sliding windows 最大值
    # 最多两种不同的水果, windows中distrink number >2 shrink windows
    def totalFruit(self, fruits: List[int]) -> int:
        windows = dict()
        left , right = 0 , 0
        ans = 0
        while right < len(fruits):
            if fruits[right] in windows:
                windows[fruits[right]] += 1
            else:
                windows[fruits[right]] = 1
            # shrink windows to check answer
            while len(windows) > 2:
                windows[fruits[left]] -= 1
                if windows[fruits[left]] == 0:
                    del  windows[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

            right += 1

        return ans