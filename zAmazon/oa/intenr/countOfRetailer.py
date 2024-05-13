# https://www.fastprep.io/problems/amazon-count-number-of-retailers

'''

In a newly planned city, where a city is located at each integral coordinate in a 2-dimensional plane,
there are n Amazon retailers. The ith retailer residing in the city at the coordinate (x[i], y[i]) and can deliver to all the cities covered by the rectangle having the 4 corner points (0, 0), (x[i], 0), (0, y[i]), (x[i], y[i]). We say that a point (a, b) is covered by a rectangle if it lies inside the rectangle or on its boundaries. Note that no 2 retailers reside in the same city.

Given q requests of the form (a, b), determine the number of retailers who can deliver to the city at the coordinate (a, b).

'''
class Solution:
    def countNumberOfRetailers(self, retailers: List[List[int]], requests: List[List[int]]) -> List[int]:
        retailers.sort()  # Assuming retailers need to be sorted by the first element
        results = []

        # Each request
        for a, b in requests:
            # Binary search to find the first index where x >= a
            low, high = 0, len(retailers) - 1
            while low <= high:
                mid = (low + high) // 2
                if retailers[mid][0] < a:
                    low = mid + 1
                else:
                    high = mid - 1

            start_index = low
            count = 0

            # Count retailers whose y >= b from the found index
            for i in range(start_index, len(retailers)):
                if retailers[i][1] >= b:
                    count += 1

            results.append(count)

        return results
