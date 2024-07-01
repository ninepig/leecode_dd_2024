class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        hashmap = dict() # not default
        # build monotono stack to get each next bigger element in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack[-1]] = num
                stack.pop()
            stack.append(num)

        # find number in complexDs
        for num in nums1:
            res.append(hashmap.get(num,-1))

        return res

    ##不用hashmap 就需要用数组 index
    def nextGreaterElementsCycle(self, nums: List[int]) -> List[int]:
        # cycle_nums = nums + nums
        # 不需要两倍数组, 只需要循环2倍长度 外加 %2
        stack = []
        size =len(nums)
        res = [-1 for _ in range(size)] # not exit, we output 1

        for i in range(2*size):
            while stack and nums[i%size] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i % size]
            stack.append(i%size)

        return res