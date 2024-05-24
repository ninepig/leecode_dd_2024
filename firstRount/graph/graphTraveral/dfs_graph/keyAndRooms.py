class Solution:
    '''经典dfs 从0出发 把每次可以加入的room 加入set之中 最后判断是否长度一样'''
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(room):
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    dfs(key)
        dfs(0)
        return len(rooms) == len(visit)