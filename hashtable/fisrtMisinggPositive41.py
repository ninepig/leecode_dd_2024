'''原地哈希的概念 非常好的题
但这道题太苛刻了。。就是为了考原地哈希的概念'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)

        '''
        https://www.youtube.com/watch?v=cG1rZPIo3ww&ab_channel=%E5%82%85%E7%A0%81%E7%88%B7
        把数放在对应的index上，比如 index 0 就应该放 1 index 1 就该放2 
        满足这种情况 就是 num[i] == num[num[i] - 1]
        利用index的数值去array里找值
        然后把非正整数放到数组中不存在value的index上
        比如[-1,2,1,3]---->[1,2,3,-1]'''
        for i in range(size):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                index1 = i
                index2 = nums[i] - 1
                nums[index1], nums[index2] = nums[index2], nums[index1]

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1