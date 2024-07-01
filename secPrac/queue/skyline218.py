from sortedcontainers import SortedList

'''
可以看出来：关键点的横坐标都在建筑物的左右边界上。

我们可以将左右边界最高处的坐标存入 points 数组中，然后按照建筑物左边界、右边界的高度进行排序。

然后用一条条「垂直于 x 轴的扫描线」，从所有建筑物的最左侧依次扫描到最右侧。从而将建筑物分割成规则的矩形。

不难看出：相邻的两个坐标的横坐标与矩形所能达到的最大高度构成了一个矩形。相邻两个坐标的横坐标可以从排序过的 points 数组中依次获取，矩形所能达到的最大高度可以用一个优先队列（堆）max_heap 来维护。使用数组 ans 来作为答案答案。

在依次从左到右扫描坐标时：

当扫描到建筑物的左边界时，说明必然存在一条向右延伸的边。此时将高度加入到优先队列中。
当扫描到建筑物的右边界时，说明从之前的左边界延伸的边结束了，此时将高度从优先队列中移除。
因为三条高度相同的线应该合并为一个，所以我们用 prev 来记录之前上一个矩形高度。

如果当前矩形高度 curr 与之前矩形高度 prev 相同，则跳过。
如果当前矩形高度 curr 与之前矩形高度 prev 不相同，则将其加入到答案数组中，并更新上一矩形高度 prev 的值。
最后，输出答案 ans
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        pq = SortedList()
        points = [] #
        pre = 0 # record prev height, if we got same height point, we only output once in skyline
        for build in buildings:
            left, right, height = build[0], build[1],build[2]
            points.append([left,-height])
            points.append([right,height])

        points.sort(key=lambda x:(x[0],x[1]))# sorted by x ray first then y ray , make sure left node is priorir than right node

        for point in points:
            x, height = point[0],points[1]
            if height < 0:
                pq.add(-height) # adding height to queue
            else:
                pq.remove(height) # if we reach the right side of one point, we need to remove that out of point

            cur = pq[-1]
            if cur != pre :# if height not equal to pre
                ans.append(x,cur)
                pre = cur

        return ans
