class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) > len(goal) : return False
        s2 = s + s
        return s2.find(goal) != -1