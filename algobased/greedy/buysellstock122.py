'''
只有122是贪心
别的都是动规
'''
'''因为我们只能吃有一个股票,策略就变了
只要赚钱我们就进行操作. 看最多能赚多少'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i]-prices[i-1])
        return ans