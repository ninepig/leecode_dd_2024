class solution:
    '''
    https://leetcode.cn/problems/product-of-array-except-self/solutions/11472/product-of-array-except-self-shang-san-jiao-xia-sa
    '''
    def getMulArray(self,arr:list[int]):
        ## 这个题要画一个表格来做, 利用返回的空间来作为临时变量
        ans = [1] * len(arr)
        temp = 1
        ## cal arr[n-1]'s left side sum
        for i in range(1,len(arr)):
            ans[i] *= arr[i-1]

        ## cal right side arr[n+1]'s res first, then times ans
        for i in range(len(arr) - 2 , -1, -1):
            temp *= arr[i + 1]
            ans[i] *= temp

        return ans