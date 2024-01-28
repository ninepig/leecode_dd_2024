class Solution:
    # counting sort
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_min = min(arr1)
        arr1_max = max(arr1)
        count = [0 for _ in range(arr1_max - arr1_min + 1)]
        # count
        for num in arr1:
            count[num - arr1_min] += 1

        res = []
        # check order in num2
        for num in arr2:
            while count[num - arr1_min] > 0: # if num1 has couple duplicated element, need order like num2
                res.append(num)
                count[num - arr1_min] -= 1

        ## asdc oder to output num in number1
        for i in len(count):
            while count[i] > 0:
                res.append(i + arr1_min)
                count[i] -= 1

        return res