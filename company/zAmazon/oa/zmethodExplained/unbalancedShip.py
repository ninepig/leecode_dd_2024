# https://www.fastprep.io/problems/amazon-maximum-number-of-shipments
'''
Amazon has multiple delivery centers for the distribution of its goods. In one such center, parcels are arranged in a sequence where the ith parcel has a weight of weight[i].

A shipment is constituted of a contiguous segment of parcels in this arrangement. That is, for 3 parcels arranged with weights [3, 6, 3] a shipment can be formed of parcels with weights [3], [6], [3], [3, 6], [6, 3] and [3, 6, 3] but not with weights [3, 3]. These shipments are to be loaded for delivery and must be balanced.

A shipment is said to be balanced if the weight of the last parcel of the shipment is not the maximum weight among all the weights in that shipment. For example, shipment with weights [3, 9, 4, 7] is balanced since the last weight is 7, while the maximum shipment weight is 9. However, the shipment [4, 7, 2, 7] is not balanced.

Given the weights of n parcels placed in a sequence, find the maximum number of shipments that can be formed such that each parcel belongs to exactly one shipment, each shipment consists of only a contiguous segment of parcels, and each shipment is balanced. If there are no balanced shipments, return 0.

Function Description

Complete the function maxNumberOfBalancedShipments in the editor.

maxNumberOfBalancedShipments has the following parameter:

int[] weights: an array of integers representing the weights of the parcels
Returns

int: the maximum number of balanced shipments that can be formed
'''
from typing import List

'''
脑经急转弯
'''

class Solution:
    def maxNumberOfBalancedShipments(self, weights: List[int]) -> int:
        max_weight = float('-inf')
        shipments = 0
        ## 如果有一个小于最大weight 那就多一个shipment ，同时maxweight置-1，此时已经有至少2个了。 所以可以组成一个shipment
        ## max 》 weight
        ## 贪心法
        for weight in weights:
            if weight < max_weight:
                shipments += 1
                max_weight = -1
            else:
                max_weight = max(max_weight, weight)
        ## check last one
        if max_weight != -1 and weights[-1] != max_weight:
            shipments += 1

        return shipments

sol = Solution()
test = [4, 3, 6, 5, 3, 4, 7, 1]
print(sol.maxNumberOfBalancedShipments(test))