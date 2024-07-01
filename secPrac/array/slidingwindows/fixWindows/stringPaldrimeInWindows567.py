import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        s1_counter = collections.Counter(s1)
        windows_counter = collections.Counter()
        windows_lens = len(s1)

        while right < len(s2):
            # 利用一个 windowscounter来统计字符出现次数，
            windows_counter[s2[right]] += 1
            if right - left + 1 >= windows_lens:
                if windows_counter == s1_counter : #如果和目标S1的counter一样，则说明他们是同排列
                    return True
                #从左侧开始删除 couter
                windows_counter[s2[left]]-=1
                if windows_counter[s2[left]] == 0:
                    del windows_counter[s2[left]]
                left += 1

            right += 1

        return False