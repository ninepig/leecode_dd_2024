class Solution:
    '''滑动数组，看k之内得分'''
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left , right = 0, 0
        score = 0
        windows_sum = 0
        while right < len(calories):
            windows_sum +=calories[right]
            if right - left + 1 >= k:
                if windows_sum > upper:
                    score -=1
                elif windows_sum < lower :
                    score += 1
                windows_sum -= calories[left]
                left += 1
            right += 1

        return score