class Solution:
    '''因为计算出现的数量， 所以可以用hashtbale来做 add1 + add2 = -(add3 + add4)'''
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums_dict = dict()
        for num in nums1:
            for num2 in nums2:
                sum12 = num + num2
                if sum12 in nums_dict:
                    nums_dict[sum12] +=1
                else:
                    nums_dict[sum12] = 0
        count = 0
        for num in nums3:
            for num2 in nums4:
                sum34 = - (num + num2)
                if sum34 in nums_dict:
                    count += nums_dict[sum34]

        return count

