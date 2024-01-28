class Solution:
    '''快慢指针 答案太精美了'''
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        slow , fast = 0 , 0
        while fast < size :
            #节省space ， 把快的char,因为快的char是第一次出现在现在这个情况下 所以给慢的赋值
            # 类似abc 第一次出现的a
            chars[slow] = chars[fast]
            count = 1
            while fast + 1 < size and chars[fast] == chars[fast+1]:
                count += 1
                fast += 1

            if count > 1 :
                for c in str(count):
                    chars[slow+1] = c
                    slow += 1

            fast += 1
            slow += 1

        return slow

