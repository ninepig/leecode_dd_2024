'''
复杂一点的 fix K
把问题转换成 固定窗口的最小值
这样剩下的5个就可以是最大的
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        window_sum = 0
        cards_sum = sum(cardPoints)
        min_sum = cards_sum

        left, right = 0, 0
        if window_size == 0:
            return cards_sum

        while right < len(cardPoints):
            window_sum += cardPoints[right]

            if right - left + 1 >= window_size:
                min_sum = min(window_sum, min_sum)
                window_sum -= cardPoints[left]
                left += 1

            right += 1

        return cards_sum - min_sum