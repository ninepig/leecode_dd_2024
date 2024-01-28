from LinkedList import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # initl every kid has 1 candy
        # if rate[i-1] < rate[i] i have one more candy
        # if rate[i] > rate[i+1] i have at least one more candy
        size = len(ratings)
        candy = [1 for _ in range(size)]
        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(size - 2 , -1 , -1):
            if ratings[i + 1] < ratings[i]:
                candy[i] = max(candy[i],candy[i+1] + 1)

        res = sum(candy)

        return res