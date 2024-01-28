'''
经典快慢指针
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        slow, fast = 0, 1

        while (fast < len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

        '''在原数组空间基础上删除重复出现 
    2 次以上的元素，并返回删除后数组的新长度。
    '''

    class Solution:
        #一次遍历的牛逼做法
        def removeDuplicates(self, nums: List[int]) -> int:
            size =  len(nums)
            if size < 2 :
                return size
            slow , fast = 2, 2
            while fast < size:
                #妙手，因为当fast-2 == slow 的时候， slow = slow + 1 = slow +2 fast指针不需要保留
                if nums[fast - 2] != nums[slow]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1

            return slow + 1

