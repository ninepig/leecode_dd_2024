# The chef processes the eligible orders one at a time and deletes the orderId processed from the array.
# In a given array of orders, an eligible orderId is the orderId that is greater than its immediate left neighbor and Immediate right neighbor.
# For the first element in the array, it is eligible if it is greater than its right neighbor; for the last element it should only be greater than its left neighbor.
# If there are more than 1 eligible orderid then chef processes the order with smaller orderid.
# Return sequence of processing the order.
#
# Eg.
#
# Initial OrderIds = [3,1,5,4,2]
#
# In first iteration 3 and 5 both eligible so take 3
# Order processed: 3
# After processing the order 3 array would look like remaining orders would be [1,5,4,2]
#
# After 2nd iteration
# In second iteration only 5 is eligible so
# Order processed: 5
# Array would [1,4,2]
#
# After 3rd iteration
# Only 4 is eligible
# Order processed:4
# Array would be[1,2]
#
# After 4th iteration
# Only eligible item is 2
# Order processed:2
# Array would be [1]
#
# Finally array would be [1]
# Order processed: 1
#
# So ans 3,5,4,2,1
'''
试试看暴力法
o(nlgn) 比较现实
'''
import heapq
import math
from heapq import heappop, heappush


def process(orders: list[int]):
##todo 暴力法 dummynode来做
    res = []
    peak_dict = dict()
    # print(orders)
    # N = len(orders)
    for i in range(len(orders)):
        # print(len(orders))
        if len(orders) == 1:
            res.append(orders[0])
            break
        peak_dict.clear()
        current_idx = -1
        small_value = math.inf
        for j in range(len(orders)):
            # print(j)
            if j == 0 and orders[j] > orders[j+1]:
                # if peak_value > orders[j]:
                peak_dict[j] = orders[j]
            if j == len(orders) - 1 and orders[j] > orders[j - 1]:
                peak_dict[j] = orders[j]
            if j != len(orders) - 1 and j != 0 and orders[j] > orders[j + 1] and orders[j] > orders[j - 1]:
                peak_dict[j] = orders[j]
        for key in peak_dict.keys():
            if peak_dict[key] < small_value:
                small_value = peak_dict[key]
                current_idx = key
        # print("peak_indx",current_idx)
        ## find lowest peak index
        res.append(orders.pop(current_idx))
        # print(orders)

    return res


def is_eligible(left,neighbour):
    if neighbour[left][0] < left and left > neighbour[left][1]:
        return True
    return False


def processPQ(orders: [int]):
    orders = [-math.inf] + orders + [-math.inf] ## dummy value for better processing
    queue = []
    ## we maintain a dict to track each node's left/right neighbour
    neighbours = dict()
    #loop value to find local peak and push to pq
    for i in range(1,len(orders) - 1):
        ## maintain a map
        neighbours[orders[i]] = [orders[i - 1], orders[i + 1]]
        if orders[i] > orders[i - 1] and orders[i] > orders[i + 1]:
            heapq.heappush(queue,orders[i])

    res = []
    while queue:
        ## 很关键。。。
        lowest_peak = heapq.heappop(queue)
        res.append(lowest_peak)
        ## maintain new neigbour map and check if left, right node can be push to queue
        left,right = neighbours[lowest_peak]
        ## make neighbour node's lefr right refer leigit
        ## check if we find a new peak with updated node
        if left != -math.inf:
            neighbours[left][1] = right
            if is_eligible(left,neighbours): heappush(queue, left)
        if right != -math.inf:
            neighbours[right][0] = left
            if is_eligible(right,neighbours):heappush(queue,right)
        neighbours.pop(lowest_peak)

    return res


print(process([30,10,50,40,20,70,15,16]))
print(processPQ([30,10,50,40,20,70,15,16]))
