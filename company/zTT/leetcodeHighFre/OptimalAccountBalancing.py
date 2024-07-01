import math
import collections

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.Counter()
        # Calculates the net balance amt each person should receive or give
        for from_, to, amt in transactions:
            balance[to] += amt
            balance[from_] -= amt
        balance = list(balance.values())
        return backtrack(balance, 0)


# - Any unsettled balances between n people can be resolved in at most n-1 transactions.
# - The number of transations possible between n people is ~ n^2.
# - So we try out all the possible ways to pick at most n-1 transations from the n^2 available
# - Note that this sounds like the total possibilities are ~ O(n^2 CHOOSE n)
#   but as noted below, once we pick a transaction, we remove all other transactions that
#   include the originating node of the transaction since we don't want to any loops (Creating a loop with n-1 transations will lead to unsettled debts).
# - Essentially this means that the first level of recursion has n - 1 choices, second level has n - 2 and so on

# - Each transaction we pick settles the balance of at most 2 people
# - We prune the search by not picking transactions that don't settle the balance of anyone
#   eg transation between someone who is settled and and an unsettled person
# - Another way to prune is not to settle between person of same sign since at best it will not improve
#   on optimal solution and at worst will be sub optimal
def backtrack(arr, index):
    # At each level we settle the debt of person at index
    # If it is already settled, pick next non settled person
    if index == len(arr):
        return 0
    if not arr[index]:
        return backtrack(arr, index + 1)

    min_txns = math.inf
    # Try all possible transactions originating at index and ending between index...len(arr)
    for j in range(index + 1, len(arr)):
        # Pruning. arr[j] must be non zero and of different sign
        ## 只有两个账户一个正一个负 才有必要去transaction
        if (arr[j] * arr[index]) < 0:
            arr[j] += arr[index]
            min_txns = min(1 + backtrack(arr, index + 1), min_txns)
            arr[j] -= arr[index]
    return min_txns