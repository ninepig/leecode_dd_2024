class Solution:
    '''纯技巧题 贪心
    暴力法肯定easy'''
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float['inf']
        # 只要出现3连
        for num in nums:
            if num < a :
                a = num
            elif num < b:
                b = num
            else:
                return True
        return False