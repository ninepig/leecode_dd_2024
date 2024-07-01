# https://www.fastprep.io/problems/amazon-reduce-gifts

'''
New Year's Day is around the corner and Amazon is having a sale.
They have a list of items they are considering but they may need to remove some of them.
 Determine the minimum number of items to remove from an array of prices so that the sum of prices of any k items does not exceed a threshold.

'''
# INPUT
# prices = [3, 2, 1, 4, 6, 5]
# k = 3
# threshold = 14
# prices= [9, 6, 7, 2, 7, 2]
# k= 2
# threshold= 13

## invalid
# prices= [9, 6, 3, 2, 9, 10, 10, 11]
# k= 4
# threshold= 1

# prices= [10, 8, 12, 15, 20, 5]
# k= 3
# threshold= 25

# prices.sort()
# ans = 0
# ## 大于等于的话 多走一次，因为可能就算只有k个元素 也无法满足 大于threadhold ， improving by wenjing
# while len(prices) >= k:
# # while len(prices) > k:
#     sum_last_k = sum(prices[-k:])
#     if sum_last_k > threshold:
#         prices.pop()
#         ans += 1
#     else:
#         break #found a solution just break the loop
#
# print(ans)


import heapq
class Solution:
  def reduceGifts(self, prices: list[int], k: int, threshold: int) -> int:
    size = len(prices)
    if size <= k:
      return 0

    # Construct a max Heap
    maxStack = []
    for price in prices:
      heapq.heappush(maxStack, -price)

    counter = 0
    while len(maxStack) >= k and sum(heapq.nsmallest(k, maxStack)) < -threshold:
      heapq.heappop(maxStack)
      counter += 1

    return counter

sol = Solution()
# prices = [9, 6, 7, 2, 7, 2]
#
# k = 2
# threshold = 13

# prices = [3, 2, 1, 4, 6, 5]
# k = 3
# threshold = 14

prices = [9, 6, 3, 2, 9, 10, 10, 11]
k = 4
threshold = 1


print(sol.reduceGifts(prices,k,threshold))