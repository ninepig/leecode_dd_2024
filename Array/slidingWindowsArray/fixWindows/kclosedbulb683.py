class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        size = len(bulbs)
        days = [0 for i in range(size)]
        for i in range(size):
            days[bulbs[i] - 1] = i + 1

        left , right = 0 , k + 1

        ans = float('inf')

        while right < size :
            check_flag = True
            for i in range(left + 1 , right):
                # 保证每一天都是关灯状态, 如果有一天不是，则是false
                if days[i] < days[left] and days[i] < days[right]:
                    left , right = i , i + k + 1
                    check_flag = False
                    break
                if check_flag:
                    # days left , days right 表示 左右两个灯泡开灯时间较晚的那天
                    ans = min(ans,max(days[left],days[right]))
                    left, right = right, right + k + 1

        if ans != float('inf'):
            return  ans
        else:
            return  -1