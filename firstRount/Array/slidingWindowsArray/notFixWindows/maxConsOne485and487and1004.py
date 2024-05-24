class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

    '''
暴力做法是尝试将每个位置的 0 分别变为 1，然后统计最大连续 1 的个数。但这样复杂度就太高了。

我们可以使用滑动窗口来解决问题。保证滑动窗口内最多有 1 个 0。具体做法如下：

设定两个指针：left、right，分别指向滑动窗口的左右边界，保证滑动窗口内最多有 1 个 0。使用 zero_count 统计窗口内 1 的个数。使用 ans 记录答案。

一开始，left、right 都指向 0。
如果 nums[right] == 0，则窗口内 1 的个数 + 1。
如果该窗口中 1 的个数多于 1 个，即 zero_count > 1，则不断右移 left，缩小滑动窗口长度，并更新窗口中 1 的个数，直到 zero_count <= 1。
维护更新最大连续 1 的个数。然后右移 right，直到 right >= len(nums) 结束。
输出最大连续 1 的个数。

    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left , right = 0, 0
        ans = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1 :
                if nums[left] == 0 :
                    zero_count -= 1
                left += 1
            # windows length
            ans = max(ans, right - left + 1)
            right += 1

        return ans

    '''
    we can flip k 0 to 1 at max , how many 1 in row
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0 , 0
        size = len(nums)
        zero_count = 0
        max_len = -1
        while right < size:
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k :
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len if max_len != -1 else 0