class Solution:
    #逆向思维， 如果前后拿k， 也就是中间段 size - k 的牌点数最小
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = 0
        target_size = len(cardPoints) - k
        point = float('inf')
        point_sum = 0

        # miss one step
        if target_size == 0:
            return point

        while right < len(cardPoints):
            point_sum += cardPoints[right]
            if right - left + 1 == target_size:
                point = min(point,point_sum)
                point_sum -= cardPoints[left]
                left += 1

            right += 1

        return sum(cardPoints) - point