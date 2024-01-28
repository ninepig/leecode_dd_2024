class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brual force
        # count = 0
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i + 1 ,size):
        #         if sum(nums[i:j]) == k:
        #             count += 1
        # return count
        '''
        pre_sum[i] 的定义是前 i 个元素和，则 pre_sum[i] 可以由 pre_sum[i - 1] 递推而来，
        即：pre_sum[i] = pre_sum[i - 1] + num[i]。
        [j..i] 子数组和为 k 可以转换为：pre_sum[i] - pre_sum[j - 1] == k。
        综合一下，可得：pre_sum[j - 1] == pre_sum[i] - k 。
        所以，当我们考虑以 i 结尾和为 k 的连续子数组个数时，只需要统计有多少个前缀和为 pre_sum[i] - k （即 pre_sum[j - 1]）的个数即可。具体做法如下

        因为求的是数组区间和. 所以要想到用presum数组
        '''
        pre_dict = {0:1}
        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num
            # 如果之前已经出现过
            if pre_sum - k in pre_dict:
                count += pre_dict[pre_sum - k]
            if pre_sum in pre_dict:
                pre_dict[pre_sum] += 1
            else:
                pre_dict[pre_sum] = 1

        return count