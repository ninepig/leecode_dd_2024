

class Solution:
    # 暴力法 o(m)*(n)*o(min(m,n))
    #虽然是暴力法 但是很优雅.写的也很好看
    def findLengthBural(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    subLen = 1
                    while i + subLen < len(nums1) and j + subLen < len(nums2) and nums1[i+subLen] == nums2[j + subLen]:
                        subLen += 1

                    res = max(res,subLen)
        return res

    ##利用固定 num1/num2 找overlap
    #像一把尺一样, 从i位置开始
    '''
    固定1 
    nums1 =             [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    从 7开始比较
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =    [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =       [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =          [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =             [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =                [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =                   [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =                      [3, 2, 1, 4, 7]
    
    nums1 =             [1, 2, 3, 2, 1]
    nums2 =                         [3, 2, 1, 4, 7]
'''
    def findLengthTwoPointer(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        size1= len(nums1)
        size2 = len(nums2)
        for i in range(size1):
            res = max(res, self.findComman(nums1,nums2,i,0))
        for i in range(size2):
            res = max(res, self.findComman(nums1,nums2,0,i))

        return res



    def findComman(self,nums1: List[int], nums2: List[int],index1, index2):
        size1 = len(nums1)
        size2 = len(nums2)
        cur_leng = 0
        max_leng = 0
        while index1 < size1 and index2 < size2:
            if nums1[index1] == nums2[index2]:
                cur_leng += 1
                max_leng = max(cur_leng,max_leng)
            else:
                cur_leng = 0
            index1 += 1
            index2 += 2

        return max_leng

    '''
    dp的方法 最简洁,但是时间复杂度 空间复杂度一般'''
    def findLengthDp(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        res = 0
        ## initial and state
        dp = [[0 for _ in range(size1 + 1)] for _ in range(size2 + 1)]
        for i in range(size1 + 1):
            for j in range(size2 + 1):
                # 很简单的状态转移. 
                if nums1[i-1] == nums2[j-1]:# 只有当前一位相同时, dp才能+1, 因为subarray value相同,
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]

        return res
