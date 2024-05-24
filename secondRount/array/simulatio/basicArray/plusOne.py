class solution:
    ## 这个做法是非常经典的模拟
    ## 新建一个数组 用来处理极端情况， 从后往前进位
    def addOne(self,arr:list[int]):
        if not arr or len(arr) == 0:
            return 1
        arr = [0] + arr ## form arry with a prefix , just in case all 9 condition
        ## adding 1 operation
        arr[len(arr) - 1] += 1
        for i in range(len(arr) - 1 , -1 ,-1):
            if arr[i] == 10:
                arr[i] = 0
                arr[i-1] += 1
            else:
                break

        if arr[0] != 1:
            return arr[1:]
        return arr