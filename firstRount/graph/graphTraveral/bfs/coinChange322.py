'''
bfs version
'''
import collections


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = collections.deque([])
        step = 0
        visited = set()
        visited.add(amount)
        queue.append(amount)

        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                # 对每一个都进行操作，bfs
                cur = queue.popleft()
                for coin in coins:
                    # 能够凑成目标数量
                    if cur == coin:
                        step += 1
                        return step
                    elif cur > coin and cur - coin not in visited:
                        visited(cur - coin)
                        queue.append(cur - coin)

        return -1