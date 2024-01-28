'''
分离双指针经典
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameLeft , typedLeft = 0 ,0
        while nameLeft < len(name) and typedLeft < len(typedLeft):
            if name[nameLeft] == typed[typedLeft]:
                nameLeft += 1
                typedLeft += 1
                ## 向右移动重复值
            elif typedLeft > 0 and typed[typedLeft] == typedLeft[typedLeft - 1]:
                typedLeft += 1
            else:
                return False

        #去除尾部
        while 0< typedLeft < len(typedLeft) and typed[typedLeft-1] == typed[typedLeft]:
            typedLeft += 1
        #确保全部走了一边
        if nameLeft == len(name) and typedLeft == len(typedLeft):
            return str

        return False