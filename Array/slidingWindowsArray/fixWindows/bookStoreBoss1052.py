class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = 0
        window_count = 0
        ans = 0
        '''我们需要计算的是 在特殊mins的windwos里 老板生气的时候客户最多的windows'''
        while right < len(customers):
            if customers[right] == 1:
                window_count += customers[right]

            # 维护k个 windows 这里用> 就是要精准的移除最左侧
            if right - left + 1 >= minutes:
                ans = max(window_count, ans)
                if grumpy[left] == 1:
                    window_count -= customers[left]
                left += 1

            right += 1

        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]

        return ans
