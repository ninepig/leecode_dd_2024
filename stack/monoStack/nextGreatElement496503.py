class Solution:
    '''
    描述：给定两个没有重复元素的数组 nums1 和 nums2 ，其中 nums1 是 nums2 的子集。

要求：找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
    递增栈的标准做法
    递增栈, 右侧
    ---> 第一个大的就是要入栈的元素
    公式
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        numDict = dict()
        for num in nums2:
            while stack and num > stack[-1]:
                numDict[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in nums1:
            res.append(numDict.get(num,-1))

        return res
    '''
    数组循环的技巧,让他两倍即可
    '''
    def nextGreaterElement(self, nums1: List[int]) -> List[int]:
        stack = []
        res = []
        size = len(nums1)
        for i in range(size):
            while stack and nums1[i % size] > stack[-1]:
                index = stack.pop()
                res[index] = nums1[i % size]
            stack.append(i % size)

        return res
