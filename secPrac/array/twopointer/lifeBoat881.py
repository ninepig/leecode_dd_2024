class Solution:
    # need make sure max peopal < limit
    # 贪心
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        if max(people) > limit : return -1 # no way to get
        res = 0
        left = 0
        right = len(people) - 1
        people.sort()
        while left < right:
            # only one people get boat
            if people[left] + people[right] > limit:
                res += 1
                right -= 1
            else: # can 2 people get on boat
                res += 1
                right -= 1
                left += 1
        if left == right: # need one more boat , point to same people
            res += 1
        return res
