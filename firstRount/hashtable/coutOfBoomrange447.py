'''经典数学题 + complexDs
x---》y z 点的距离存入hashmap之中
关键是ans的计算'''
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        # 不需要index 所以直接 for each 即可
        for pointx in points:
            dis_dict = []
            for pointy in points:
                if pointy != pointx:
                    dx = pointy[0] - pointx[0]
                    dy = pointy[1] - pointx[1]
                    dis = dy**2 + dx**2
                    if dis in dis_dict:
                        dis_dict[dis] += 1
                    else:
                        dis_dict[dis] = 1
            ## 统计答案， 如果某个距离的value是5 那就要计算他的组合 5*（5-1） 可能性
            for value in dis_dict.values():
                ans += value * (value - 1)
        return ans
