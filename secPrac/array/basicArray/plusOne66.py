'''o(n) time
o(1) inplace or o(n)  if we create extra '''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits :
            return []
        size = len(digits)
        # loop from last to first

        for i in range(size - 1 , -1 , -1 ):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        res = [0 for _ in range(size + 1)]
        res[0] = 1
        return res

    def plusOneAnseswer(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # 这个方法比较好, 不需要重新做数组
        digits.append(0)
        digits[0] = 1
        return digits