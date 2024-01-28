class Solution:
    '''三指针的方法太清晰了
    快慢 + index'''
    def compress(self, chars: List[str]) -> int:
        if not chars or len(chars) == 0:
            return 0
        slow , write = 0,0
        size = len(chars)
        while slow < size:
            fast = slow
            ## move right find similar char
            while fast  < size and chars[fast] == chars[slow]:
                fast += 1

            chars[write] = chars[slow] ## put first slow char
            write += 1

            if fast - slow > 1 :# we have more than 1 same char
                for c in str(fast - slow):
                    chars[write] = c
                    write += 1
            slow = fast

        return write