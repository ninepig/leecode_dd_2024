from LinkedList import List


class Solution:
    ## 排序 + 检查
    ## hashset
    def longestConsecutive(self, nums) -> int:
        nums.sort()
        local = 1
        ans = 1
        for i in range(1,len(nums)):
            if nums[i - 1] + 1== nums[i]:
               local += 1
               ans = max(ans,local)
            else:
                local = 1

        return ans

    # 自己的写法有点蠢
    def longestConsecutive2(self, nums) -> int:
        # nums_set = set(nums)
        # ans = 1
        # res = 1
        # for num in nums_set:
        #     while  (num + 1) in nums_set:
        #         ans += 1
        #         res = max(res,ans)
        #         num += 1
        #
        # return ans

    def longestConsecutiveMap(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                ans = max(ans, curr_streak)

        return ans


if __name__ == "__main__":
    test = [1,2,4,3]
    lc = Solution()
    print(lc.longestConsecutive(test))
