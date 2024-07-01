class Solution:
    def popLocalPeak(self,nums: list[int]):
        '''
        个人出题
        [3 5 1 4 2]
        local peak
        [4,2,5,3,1]
        '''
        ## brutal force way
        ## from end to start if array exist
        # each time pop a local peak
        # not bf way
        #
        # 1. linear scan 把所有的 local peak 放进 stack 里面
        # 2. 每次从stack pop 的时候检查左右两边是否成为新的 local peak, 然后放进 stack
        #
        res = []
        while len(nums) != 0:
            print(nums)
            if len(nums) == 1: ## only one digit lefet
                res.append(nums[0])
                break
            if len(nums) == 2:
                if nums[i] < nums[i - 1]:
                    res.append(nums[i - 1])
                    nums.pop(i - 1)
                    continue
                else:
                    res.append(nums[i])
                    nums.pop(i)
                    continue
            for i in range(len(nums) - 1, -1 , -1): # reverse from back
                if i + 1 == len(nums) and nums[i] > nums[i-1]: # last digist, and last digist is a peak
                    res.append(nums[i])
                    nums.pop(i) ## removed this index from num
                    break
                elif nums[i-1] < nums[i] > nums[i+1]:
                    res.append(nums[i])
                    nums.pop(i)
                    break
                elif nums[i] == 0: ## no peak from end, first is peak
                    res.append(nums[i])
                    nums.pop(i)
                    break
        return res

    ## https://leetcode.com/discuss/interview-question/4154082/Doordash-or-Phone-or-Eligible-order-sequence/
    def process_orders(self,orders):
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


num =  [3, 5, 1, 4, 2]
#
# for i in range(len(num) - 1, -1, -1):
#     print(num[i])
#     num.pop(i)

test = Solution()
print(test.process_orders(num))
