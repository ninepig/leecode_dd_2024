class Solution:
    '''双指针，向左右衍生 ，找到满足最长的山脉 ， o(n2)'''
    def longestMountain(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0 : return 0
        ans = float('-inf')
        size = len(arr)
        for i in range(1,size-1):
            left = i - 1
            right = i + 1
            while left >= 0 and arr[left] < arr[i]:
                left -= 1

            while right < size and arr[right] < arr[i]:
                right += 1

            ans = max(ans,right - left + 1)

        return ans