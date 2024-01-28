import collections

'''
标准的bfs
有一定难度'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        quque = collections.deque(['0000'])
        visited = set()
        deadset = set(deadends)
        level = 0

        while quque:
            size = len(quque)
            for i in range(size):
                cur = quque.popleft()
                if cur in deadset:
                    continue
                if cur == target:
                    return level
                for i in range(len(cur)):
                    # two operations -> up and down
                    up = self.upward_adjust(cur,i)
                    if up not in visited:
                        visited.add(up)
                        quque.append(up)
                    down = self.down_adjust(cur,i)
                    if down not in visited:
                        visited.add(down)
                        quque.append(down)
            level += 1

        return -1

    def upward_adjust(self, cur, i):
        list_s = list(cur)
        if  list_s[i] == '9':
            list_s[i] = '0'
        else:
            list_s[i] = chr(ord(list_s[i]) + 1)
        return ''.join(list_s)

    def down_adjust(self, cur, i):
        list_s = list(cur)
        if list_s[i] == '0':
            list_s[i] = '9'
        else:
            list_s[i] = chr(ord(list_s[i]) + 1)
        return ''.join(list_s)

