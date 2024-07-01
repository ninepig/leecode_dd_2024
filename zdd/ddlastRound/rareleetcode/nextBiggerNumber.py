'''
next bigger number / positive / negative
记忆题
'''
class solution:
    '''
    137652
    find first number num[i - 1] < num[i] from end of array
    3
    reverse the later part
    132567
    start from 3
    find first item bigger than 3
    152367
    this is next bigger one
    '''
    def nextBiggerNumber(self,target:int)->int:
        if target <= 0 :
            # raise Exception("wrong input")
            return -1
        arrays = [int(i) for i in str(target)]
        length = len(arrays)
        i = length - 1
        while i > 0 and arrays[i - 1] >= arrays[i]:
            i -= 1
        # 987654321
        if i == 0 :
            # raise  Exception("not exist")
            return -1
        self.reverse(arrays,i,length-1)
        ## i point to 2 in 132567 's case
        #if i > 0 : ## no need for this , since i must bigger
        for j in range(i,length):
            if arrays[j] > arrays[i - 1] : # find first number biggher than i
                self.swap(arrays,i-1,j)
                break
        res = sum(d * 10 ** i for i, d in enumerate(arrays[::-1]))
        return res if res < 2 ** 31 else -1 #越界 很重要turn sum([d*10**i for d,i in enumerate(arrays[::-1])])

    def reverse(self,arrays,firstidx,lastidx):
        while firstidx < lastidx:
            arrays[firstidx],arrays[lastidx] = arrays[lastidx],arrays[firstidx]
            firstidx += 1
            lastidx -= 1
    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]


    '''
    previous permutation
    13245 
    从后往前找 第一个 num[i-1] > num[i]的。 最大的i值
    找到3
    然后把3往后的reverse 
    13542
    然后把3 和 2交换（第一个比他小的数） ，就和next permutation相反
    12543 这个就是previous permutation了
    '''
    def previousSmallerElement(self, target: int) -> int:
        if target < 0:
            target =  target * (-1)
        nums = [int(x) for x in str(target)]
        n = len(nums)
        i = n - 1
        idx = 0
        while i > 0 :
            if nums[i - 1] > nums[i]:
               idx = i - 1
               break
            i -= 1
        if i == 0 :
            return -1 # no previous permutation
        ## reverse number from idx
        self.reverse(nums,idx + 1 , n - 1)
        ## search first element smaller than num[idx]
        for j in range(idx+1, n):
            if nums[j] < nums[idx]:
                self.swap(nums,j,idx) # sawp 3 and 2
                break
        res = sum(d * 10 ** i for i, d in enumerate(nums[::-1]))
        return res * (-1)

number = 101
sol = solution()
print(sol.nextBiggerNumber(number))

