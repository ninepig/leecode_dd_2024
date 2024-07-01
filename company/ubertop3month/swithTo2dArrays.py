class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            temp = list(set(nums))
            res.append(temp)
            for i in temp:
                nums.remove(i)
        return res


# 作者：KBKIKK
# 链接：https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/2246472/bu-duan-xiang-da-an-zhong-tian-jia-qu-zh-yygd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
##https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions/description/