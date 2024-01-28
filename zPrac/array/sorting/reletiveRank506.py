import heapq




class Solution:
    # 需要的是相对位置
    def findRelativeRanks(self, nums):
            pairs = []
            for i in range(len(nums)):
                pairs.append([nums[i], i])
            pairs.sort(key=lambda a: a[0], reverse=True)
            for i in range(len(nums)):
                if i == 0:
                    nums[pairs[i][1]] = "Gold Medal"
                if i == 1:
                    nums[pairs[i][1]] = "Silver Medal"
                if i == 2:
                    nums[pairs[i][1]] = "Bronze Medal"
                if i > 2:
                    nums[pairs[i][1]] = str(i + 1)
            return nums


score = [10,3,8,9,4]
test = Solution()
print(test.findRelativeRanks(score))