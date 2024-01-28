class Solution:
    '''
    使用变量 ans 保存最长山脉长度。
    遍历数组，假定当前节点为山峰。
    使用双指针 left、right 分别向左、向右查找山脉的长度。
    如果当前山脉的长度比最长山脉长度更长，则更新最长山脉长度。
    最后输出 ans。
    '''
    def longestMountain(self, arr: List[int]) -> int:
        size = len(arr)
        res = 0
        for i in range(1 , size - 1):
            # assume i is peak
            if arr[i] > arr[i -1] and arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1

                while left > 0 and arr[left - 1] < arr[left] :
                    left -= 1
                while right < size - 1 and arr[right] < arr[right+1]:
                    right += 1

                if right - left + 1 > res:
                    res = right - left + 1

        return res