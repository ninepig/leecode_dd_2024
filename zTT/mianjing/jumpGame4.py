#https://leetcode.cn/problems/jump-game-iv/description/
from collections import deque, defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ##同value的list ，便于后面跳
        idxSameValue = defaultdict(list)
        for i, a in enumerate(arr):
            idxSameValue[a].append(i)
        visitedIndex = set()
        q = deque()
        ##从 0 开始跳
        q.append([0, 0])
        ## vistied 数组
        visitedIndex.add(0)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1
            for i in idxSameValue[v]:
                if i not in visitedIndex:
                    visitedIndex.add(i)
                    ## same value's index, so you can jumpto
                    q.append([i, step])
            del idxSameValue[v]
            if idx + 1 < len(arr) and (idx + 1) not in visitedIndex:
                visitedIndex.add(idx + 1)
                q.append([idx+1, step])
            if idx - 1 >= 0 and (idx - 1) not in visitedIndex:
                visitedIndex.add(idx - 1)
                q.append([idx-1, step])

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/jump-game-iv/solutions/1220752/tiao-yue-you-xi-iv-by-leetcode-solution-zsix/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。