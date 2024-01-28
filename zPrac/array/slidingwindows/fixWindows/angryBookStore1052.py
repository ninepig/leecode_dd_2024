class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = 0
        angry_window = 0
        res = 0
        while right < len(grumpy):
            ## 满足条件才能加 windows 
            if grumpy[right] == 1:
                angry_window += customers[right] # angry window' customer size
            #我们只计算mins里最多能转变多少 angry的客人 所以用这么做
            if right - left + 1 >= minutes:
                res = max(res,angry_window)
                if grumpy[left] == 1:
                    angry_window -= customers[left]
                left +=1

            right += 1

        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]

        return res

