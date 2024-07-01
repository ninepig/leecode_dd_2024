class Solution:
    '''
    使用哈希表记录每两个点之间的距离。然后使用两重循环遍历坐标数组，对于每两个点 i、点 j，计算两个点之间的距离，并将距离存进哈希表中。再从哈希表中选取距离相同的关系中依次选出两个，
    作为三个点之间的距离关系 dis[i,j] = dis[i,k] ---->
，因为还需考虑顺序，所以共有 (value * value -1)
 种情况。累加到答案中
    '''
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        point_dict = dict()
        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                distance = (points[j][1] - points[i][1])**2 - (points[j][0] - points[i][0])**2
                if distance in point_dict:
                    points[distance] += 1
                else:
                    points[distance] = 1

        ans = 0
        for value in point_dict.values():
            ans += value * (value - 1)
        return ans