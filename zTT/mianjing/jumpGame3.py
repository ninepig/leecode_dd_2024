'''

Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
Notice that you can not jump outside of the array at any time.

bfs来做

https://leetcode.cn/problems/jump-game-iii/solutions/101796/tiao-yue-you-xi-iii-by-leetcode-solution/

分析题目 找到合适的算法。 模板
这个就是个经典的bfs 模板。
'''


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        used = {start}
        q = collections.deque([start])

        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)

        return False

、