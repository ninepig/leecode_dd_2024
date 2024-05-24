

class solution:
    def rotateArray(self,arr:list[int],k:int):
        ## 经典题
        ## 1234567  3
        ## 4321/765
        ## 5671234
        ## 多举例， 多做题
        if not arr or len(arr) == 0:
            return arr
        length = len(arr)
        k %= length
        ## bug
        ## length - k 而不是 length -k -1， 因为左侧是included的 而不是excluded
        self.rotate(arr,length - k, length - 1)
        print(arr)
        self.rotate(arr,0,length - k - 1)
        print(arr)
        self.rotate(arr,0,length - 1)

        return arr
    def rotate(self,arr, left, right):
        while left < right:
            ## bug
            ## python 双赋值是 等于号
            arr[left] , arr[right] = arr[right],arr[left]
            left += 1
            right -= 1

sol = solution()
arr = [1,2,3,4,5,6,7]
k = 3
print(sol.rotateArray(arr,k))