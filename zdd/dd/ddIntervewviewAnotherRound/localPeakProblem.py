'''
https://leetcode.com/discuss/interview-question/4154082/Doordash-or-Phone-or-Eligible-order-sequence/

The chef processes the eligible orders one at a time and deletes the orderId processed from the array.
In a given array of orders, an eligible orderId is the orderId that is greater than its immediate left neighbor and Immediate right neighbor.
For the first element in the array, it is eligible if it is greater than its right neighbor; for the last element it should only be greater than its left neighbor.
If there are more than 1 eligible orderid then chef processes the order with smaller orderid.
Return sequence of processing the order.

Eg.

Initial OrderIds = [3,1,5,4,2]

In first iteration 3 and 5 both eligible so take 3
Order processed: 3
After processing the order 3 array would look like remaining orders would be [1,5,4,2]

After 2nd iteration
In second iteration only 5 is eligible so
Order processed: 5
Array would [1,4,2]

After 3rd iteration
Only 4 is eligible
Order processed:4
Array would be[1,2]

After 4th iteration
Only eligible item is 2
Order processed:2
Array would be [1]

Finally array would be [1]
Order processed: 1

So ans 3,5,4,2,1

Interviwer was looking for O(n) solution.

## 这个题非常难。。
扫描过去，如果有多个 local peak， pop smaller id。。 这个也就是我们每次扫描都需要有个排序来满足
1 pq + complexDs
 1.1 pq 记录每次符合条件的local peak ---》 每次pop小的
 1.2 pop之后，利用hashmap 把popout的 左右两侧neighbour 联系在一起（类似 dqueue）， 然后再扫描， 丢入pq
 ---》 n logn 的时间复杂度

'''

## todo bf way，

from heapq import *
def process(orders: [int]):
    ## dummy node for better process
    orders = [float('-inf')] + orders + [float('-inf')]
    # min heap + complexDs approach, keep neighbor info in complexDs

    def is_eligible(order_id):
        left, right = neighbors[order_id]
        return order_id > left and order_id > right

    neighbors = dict()
    heap = []
    ## loop the array, record neighbors info into dict
    for i in range(1, len(orders) - 1):
        neighbors[orders[i]] = [orders[i - 1], orders[i + 1]]
        if orders[i] > orders[i - 1] and orders[i] > orders[i + 1]:
            heappush(heap, orders[i])

    # if we have muli candidate ---> pop the smallest
    # after pop out, check if we have new peak

    res = []
    while heap:
        order = heappop(heap)
        res.append(order)
        # update neighbors map
        left, right = neighbors[order]
        if left != float('-inf'):
            neighbors[left][1] = right
            if is_eligible(left): heappush(heap, left)
        if right != float('-inf'):
            neighbors[right][0] = left
            if is_eligible(right): heappush(heap, right)
        neighbors.pop(order)

    return res

## todo
## 如果我们pop 较小的 index 而不是pop 较小的 id 有办法吗？
## 这个方法好像可行。 就是单调栈。 第一个出栈的 明天好好做做
# i = 0
# stack = []
# result = []
# while i < len(OrderIds):
#     while stack and OrderIds[i] < stack[-1]:
#         result.append(stack.pop())    ## first item 遇到第一个单调栈pop出来的， 直接保存， 因为id最小
#     stack.append(OrderIds[i])
#     i += 1
#
# while stack:
#     result.append(stack.pop())
#
# return result

## wrong way
def process_orders_monostack(orders):
    result = []
    stack = []
    N = len(orders)
    for i in range(N):
        if i < N - 1 and orders[i] > orders[i + 1]:
            if not stack:
                result.append(orders[i])
            else:
                if orders[i] > stack[-1]:
                    result.append(orders[i])
                else:
                    while stack[-1] > orders[i]:
                        result.append(stack.pop())
                    stack.append(orders[i])
        else:
            if stack and orders[i] < stack[-1]:
                result.append(stack.pop())
            stack.append(orders[i])
    return result + stack[::-1]
# --------- driver code ---------
tests = [
    ([3,1,5,4,2], [3,5,4,2,1]),
    ([30,10,70,40,20,50,15,16], [16,30,50,70,40,20,15,10]),
    ([30,10,50,40,20,70,15,16] ,[30, 50, 40, 70, 20, 16, 15, 10]),
    ([13,4, 5, 3, 2],[5,13,4,3,2])
]

# for orders, expected in tests:
#     print('actual = {} | expected = {}'.format(process(orders), expected))
#
# for orders, expected in tests:
#     print('actual = {} | expected = {}'.format(process_orders_monostack(orders), expected))

OrderIds = [3,1,5,4,2]
i = 0
stack = []
result = []
while i < len(OrderIds):
    ## 单调递减栈， 栈顶保存的左侧第一个比你小的， 对于栈顶元素， 栈底的都比他小。 同时出现的新元素比他小，那他就是local peak
    while stack and OrderIds[i] < stack[-1]:
        result.append(stack.pop())    ## first item 遇到第一个单调栈pop出来的， 直接保存， 因为id最小
    stack.append(OrderIds[i])
    i += 1

while stack:
    result.append(stack.pop())
    #
    # return result
print(result)