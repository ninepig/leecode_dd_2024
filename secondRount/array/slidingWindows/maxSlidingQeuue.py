from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  # 双端队列
        for i, x in enumerate(nums):
            # 1. 入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 入队
            # 2. 出
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sliding-window-maximum/solutions/2499715/shi-pin-yi-ge-shi-pin-miao-dong-dan-diao-ezj6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。