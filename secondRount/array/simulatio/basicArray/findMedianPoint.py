class solution:
    ##724, 找到中心下标
    def findMedianPoint(self,arr:list[int]):
        ## 想问题想复杂了。。
        ##不需要什么prefix sum
        ## 有了sum ， 再计算左侧多大 左侧*2 + 当前元素 = sum 就是目标
        ## 这个是个脑经急转弯。
        if not arr or len(arr) == 0 : return -1
        arr_sum = sum(arr)
        left_sum = 0
        for i in range(len(arr)):
            ## 因为有负数的情况， 所以先判断，再添加， 可以避免负数的情况
            if 2 * left_sum + arr[i] == arr_sum:
                return i
            left_sum += arr[i]

        return -1
