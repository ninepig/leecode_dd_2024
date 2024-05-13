# https://www.1point3acres.com/bbs/thread-1031830-1-1.html
from heapq import heapify, heappop


class diffArray:
    def __init__(self,nums:list[int]):
        self.array = [0 for _ in range(len(nums))]
        self.array[0] = nums[0]
        for i in range(1,len(nums)):
            self.array[i] = nums[i] - nums[i - 1]

    def update(self,left:int,right:int,value:int):
        self.array[left] += value
        if right + 1 < len(self.array):
            self.array[right + 1] -= value

    def result(self):
        res = [0 for _ in range(len(self.array))]
        res[0] = self.array[0]
        for i in range(1,len(self.array)):
            res[i] = res[i-1] + self.array[i]
        return res
class Solution:
    def carPooling(self,trips: list[list[int]], capacity: int) -> bool:
        help_array = [0 for _ in range(1001)] ## set
        helper = diffArray(help_array)
        for trip in trips:
            val = trip[0]
            left = trip[1]
            right = trip[2] -1 ## trip[2] means where custmer leave, so -1 to make sure we have customer on the car
            helper.update(left,right,val)
        res = helper.result()
        for num in res:
            if num > capacity:
                return False
        return True

    ## dd problem
    def carPoolingMax(self,trips: list[list[int]]) -> int:
        help_array = [0 for _ in range(1001)] ## set
        helper = diffArray(help_array)
        for trip in trips:
            val = trip[0]
            left = trip[1]
            right = trip[2] -1 ## trip[2] means where custmer leave, so -1 to make sure we have customer on the car
            helper.update(left,right,val)
        res = helper.result()

        return max(res)

    ## 这个sorting的方法也很牛逼
    def carPoolingSortingWay(self, trips: list[list[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        max_value = 0
        for loc in lst:
            pas += loc[1]
            max_value = max(pas,max_value)
            if pas > capacity:
                print("break")
                # return False
        print(max_value)
        return True
#
test = [[2,1,5],[3,3,7]]
sol = Solution()
print(sol.carPooling(test,5))
print(sol.carPoolingMax(test))
print(sol.carPoolingSortingWay(test,5))