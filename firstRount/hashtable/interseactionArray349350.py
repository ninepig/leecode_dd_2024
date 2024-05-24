class Solution:
    '''2个set来做'''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hset = set()
        res = []
        for num in nums1:
            hset.add(num)
        for num2 in nums2:
            if num2 in hset:
                res.append(num2)

        return set(res)

    '''hashmap with counting'''
    def intersectionWithMap(self, nums1: List[int], nums2: List[int]) -> List[int]:
        htable= dict()
        res = []
        for num in nums1:
            ## 这个setDefault，如果为空 则设为1 类似 ,同理getDefault 如果不存在 则为1
            # if num not in htable:
            #     htable[num] = 1
            htable.setdefault(num,1)
        for num in nums2:
            if num in htable and htable[num] != 0:
                res.append(num)
                htable[num] -= 1

        return res


    '''Two pointer '''

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left_1 = 0
        left_2 = 0
        res = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                if nums1[left_1] not in res:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            elif nums1[left_1] > nums2[left_2]:
                left_2 += 1
        return res
#350
'''out put can be repeated
要求：返回两个数组的交集。可以不考虑输出结果的顺序。

说明：

输出结果中，每个元素出现的次数，应该与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        htable = []
        res = []
        for num in nums1:
            if num in htable:
                htable[num] += 1
            else:
                htable[num] = 1
        for num in nums2:
            if num in htable and htable[num] != 0:
                res.append(num)
                htable[num] -= 1

        return res

    
