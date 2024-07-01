'''

Pick & Delivery Permutations
1. https://leetcode.com/discuss/interview-question/1149234/DoorDash-Phone-Interview
2. https://leetcode.com/discuss/interview-question/1245761/DoorDash-Onsite
3. https://leetcode.com/discuss/interview-question/1142755/DoorDash-or-E4-or-Phone-Screen-or-Virtual-Onsite-Offer
4. https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

A driver's route can be represented as follows:
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.

A delivery cannot happen for an order before pickup.
The same order cannot be delivered or picked up twice
The car must be empty at the end of the drive.

##Pick are ascending order and delivery can be any order ？？

Examples below:
[P1, P2, D1, D2]==>valid
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
[P1, P2]==>invalid
[P1, D1, D1]==>invalid
[]==>valid
[P1, P1, D1]==>invalid
[P1, P1, D1, D1]==>invalid
[P1, D1, P1]==>invalid
[P1, D1, P1, D1]==>invalid

## 我觉得这个题 p1 必须 p2之前这个case 不解决 那就很难 所以要validate
## Pick are ascending order and delivery can be any order ## 如果有这个条件 那就先检查下这个就行了。 如果不valid 就是false
1 check if valied
2 print all permutation 第二小题 如果要做到 p1 必须 在p2 之前就挺难的
3 find longest valid path (如果是这个的话。。hashmap不就能解决吗)
4 推导所有数量的过程 https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/ rareleetcode 原题

目前看到这题有两种变形
第一种感觉比较少
1 pickup 需要排序 也就是 p1 在p2 前面
  followup 最长的valid 序列

第二种
1 任意pick up order 不需要排序
  followup 1 permutation 2 推导 公式 3 一亩三分地上有说是621的 但是我感觉不是。 应该是1359的推导 因为这个明显没有duration 这个概念。 但是可以把那个写一下

'''

## todo
def is_valid(arr):
    if arr is None or len(arr) == 0:
        return True

    if len(arr) == 1:
        return arr == ['P1', 'D1']

    pickup = set()
    completed = set()

    for i in range(len(arr)):
        order_type, num = arr[i][0], arr[i][1:]

        if order_type == 'P':
            if num in completed or num in pickup:
                return False
            pickup.add(num)
        else:
            if num not in pickup or num in completed:
                return False
            completed.add(num)

    if len(pickup) != len(completed):
        return False

    return True


def generateValidPickupDeliveriesCombination(n):
    if n is None or n == 0:
        return []

    if n == 1:
        return ['P1', 'D1']

    res = []
    pickup = set()
    delivery = set()
    dfs(n, [], res, pickup, delivery)

    return res


def dfs(n, curr, res, pickup, delivery):
    if len(curr) == n * 2:
        res.append(curr)
        return

    for i in range(n):
        if i not in pickup:
            pickup.add(i)
            dfs(n, curr + ['P' + str(i + 1)], res, pickup, delivery)
            pickup.remove(i)

    for j in range(n):
        if j in pickup and j not in delivery:
            delivery.add(j)
            dfs(n, curr + ['D' + str(j + 1)], res, pickup, delivery)
            delivery.remove(j)

    return
## 递推公式
'''
We consider the first element in all 2n elements.
The first must be a pickup, and we have n pickups as chioce.
Its pair can be any position in the rest of n*2-1 positions.
So it's (n * 2 - 1) * n.
'''
def countOrders( n):
    res, mod = 1, 10 ** 9 + 7
    for i in range(1, n + 1):
        res = res * (i * 2 - 1) * (i * 2) / 2 % mod
    return res


## 如果是 621
'''
脑筋急转弯
当存在多个任务时，由于每一类任务都需要被完成，因此本质上我们最需要考虑的是将数量最大的任务安排掉，其他任务则是间插其中。

假设数量最大的任务数为 max，共有 tot 个任务数为 max 的任务种类。

n 是冷冻时间 max是最多任务的数量。 tot 是有几个max的任务 

当任务总数 不超过 (n+1) * （max - 1） + tot 我们总能把任务插入空闲时间之中， 同时不引入额外的时间

'''
def leastInterval(self, tasks: list[str], n: int) -> int:
    cnts = [0] * 26
    for c in tasks:
        cnts[ord(c) - ord('A')] += 1
    maxv, tot = 0, 0
    for i in range(26):
        maxv = max(maxv, cnts[i])
    for i in range(26):
        tot += 1 if maxv == cnts[i] else 0
    return max(len(tasks), (n + 1) * (maxv - 1) + tot)

if __name__ == '__main__':
    print(generateValidPickupDeliveriesCombination(2))
    print(countOrders(2))