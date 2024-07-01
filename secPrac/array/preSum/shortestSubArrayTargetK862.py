from collections import deque


class Solution:
    '''是subarray 而不是连续的子数组'''
    '''
    https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solutions/1925036/liang-zhang-tu-miao-dong-dan-diao-dui-li-9fvh/
    这个解法太牛逼了太牛逼了'''
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0 for _ in range(len(nums + 1))]
        for i in range(1,len(preSum)):
            preSum[i] = preSum[i - 1] + nums[i]

        ans = len(nums) + 1
        ## brutal force
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if preSum[j] - preSum[i] >= k:
        #             ans = min(j - i + 1 , ans)
        #
        # return ans
        ## deque, 单调队列的做法,如果preSum[i] - preSum[deque[0]] >=K 满足条件, 则pop 左侧,同时比较长度
        ## 如果当前是个负数,也就是preSum[q[-1]] >= cur_s 则直接pop之前的, 因为后面的无论如何都比当前的length小,如果满足 >=k 这个条件
        queue = deque() # 双端队列,存放着index的位置
        ##单调队列
        for idx, value in enumerate(preSum): ##
            ##比较当前presum最左侧,相当于最小值
            while queue and value - preSum[queue[0]] >= k:
                ans = min(ans,idx - queue.popleft())
            ## 出现当前presum小于之前presum,也就是数为负数的情况
            while queue and preSum[queue[-1]] > value:
                queue.pop()
            queue.append(idx)

        return ans if ans < len(nums) + 1 else -1

