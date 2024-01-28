import heapq

# array = [3, 5, 1, 2, 6, 8, 7]
# #最大堆， 只要把数组变成负的就行，最后输出结果的时候再正过来即可
# array2 = [-array[i] for i in range(len(array))]
# heapq.heapify(array2)
# print(array2)
#
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# size = len(nums)
# q = [(-nums[i], i) for i in range(k)]
# heapq.heapify(q)
# print(q)
# res = [-q[0][0]]
# print(res)
# for i in range(k, size):
#     heapq.heappush(q, (-nums[i], i))
#     while q[0][1] <= i - k:
#         heapq.heappop(q)
#     res.append(-q[0][0])

array = [(0,1),(2,3),(3,4)]
for item in array:
    print(item[1])
