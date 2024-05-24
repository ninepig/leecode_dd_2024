class Solution:
    '''答案非常优雅
    关键点
    新数组第一个数需要判断是否为0
    乘法因为9*9 最大就是81， 所以第二次循环只要进一次位'''
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0" :return "0"
        num1_len , num2_len = len(num1),len(num2)
        nums = [0 for _ in range(num1_len + num2_len)]

        for i in range(num1_len - 1 , - 1 , - 1):
            digit1 = num1[i]
            for j in range(num2_len - 1 , -1 , -1):
                digit2 = num2[j]
                nums[i + j + 1] += digit2*digit1
        # 0就是到新数组的第二位， 因为我们要判断第一位是否位0
        for i in range(num1_len + num2_len -1 , 0 , -1):
            nums[i-1] += nums[i] // 10
            nums[i] %= 10
        ans = ""
        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:0] )
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans