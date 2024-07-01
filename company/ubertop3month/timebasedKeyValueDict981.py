from bisect import bisect
from collections import defaultdict

## https://leetcode.cn/problems/time-based-key-value-store/description/
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = defaultdict(list)
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        idx = bisect.bisect_right(self.times[key], timestamp)
        return self.vals[key][idx-1] if idx else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)