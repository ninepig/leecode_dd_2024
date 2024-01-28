class Solution:
    # 这题有点类似贪心. 不是双指针
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0 # global
        count = 0 # local

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                ans = max(count,ans)
            else:
                count = 0

        return ans

    # 有一个windows ,最多只有1个0
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # ans = 0
        # left,right = 0 , 0
        # windows_size = 0
        # zero_count = 0
        #
        # while right < len(nums):
        #     windows_size += 1
        #     if nums[right] == 0:
        #         zero_count += 1
        #
        #     # shrink windows
        #     while zero_count > 1:
        #         if nums[left] == 0:
        #             zero_count -= 1
        #         left += 1
        #         windows_size -= 1
        #
        #     ans = max(ans,windows_size)
        #     right += 1

        # 答案没有用windw size 直接用了 right - left +1
        left, right = 0, 0
        ans = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans


    def findMaxConsecutiveOnesMaxK(self, nums: List[int],k: int) -> int:
        left , right = 0 , 0
        flip_number = 0
        res = float('-inf')
        while right < left :
            if nums[right] == 0:
                flip_number += 1
            while flip_number > k :
                if nums[left] == 0:
                    flip_number -= 1
                left +=1

            ans = max(ans, right - left + 1)
            right += 1
        return ans
