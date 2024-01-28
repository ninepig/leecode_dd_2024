class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_table = []
        len1 = len(list1)
        len2 = len(list2)
        for i in range(len1):
            list1_table[str] = i

        minSum = len2 + len1

        for i in range(len2):
            if list2[i] in list1_table:
                index_sum = i + list1_table[list2[i]]
                if index_sum < minSum:
                    # 新建数组来取代老的
                    res = [list2[i]]
                elif index_sum == min:
                    res.append(list2[i])

        return res