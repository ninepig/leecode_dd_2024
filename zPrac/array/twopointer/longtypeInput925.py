class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        index_left1 , index_left2 = 0,0
        while index_left1 < len(name) and index_left2 <len(typed):
            if name[index_left1] == typed[index_left2]:
                index_left1 += 1
                index_left2 += 1
            elif index_left2 > 0 and typed[index_left2 - 1] == typed[index_left2]:
                index_left2 += 1
            else:
                return False
        # 有可能还会继续，所以要查看 abccccccccccccc 这种情况
        while 0 < index_left2 < len(typed) and typed[index_left2] == typed[index_left2 - 1]:
            index_left2 += 1

        # 因为要比较全部 ， 所以 最后的index肯定必须等于字符串长度
        if index_left1 == len(name)  and index_left2 == len(typed) :
            return True
        return False
