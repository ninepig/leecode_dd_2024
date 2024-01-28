class Solution:
    '''贪心 从起球的尾部开始计算
    因为贪心的原则，重叠的地方只能是前一个起球的尾部。 如果后一个气球开始大于之前的结束。就需要多一个箭'''

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points :
            return 0
        points.sort(key = lambda x : x[0])
        end_pos = points[0][1]
        count = 1
        for i in range(1,len(points)):
            if end_pos < points[i][0]:
                count += 1
                end_pos = points[i][1]

        return count