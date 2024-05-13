# https://www.fastprep.io/problems/amazon-get-max-aggregate-temperature-change
'''
Alexa is Amazon's virtual AI assistant. It makes it easy to set up your Alexa-enabled devices, listen to music, get weather updates, and much more. The team is working on a new feature that evaluates the aggregate temperature change for a period based on the changes in temperature of previous and upcoming days.

Taking the change in temperature data of n days, the aggregate temperature change evaluated on the ith day is the maximum of the sum of the changes in temperatures until the ith day, and the sum of the change in temperatures in the next (n - i) days, with the ith day temperature change included in both.

Given the temperature data of n days, find the maximum aggregate temperature change evaluated among all the days.
'''
from typing import List

## 没想明白， 不行java

##
class Solution:
  def getMaxAggregateTemperatureChange(self, tempChange: List[int]) -> int:
          left, right = tempChange[0], sum(tempChange)
          max_change = max(left, right)
          for i in range(1, len(tempChange)):
              left += tempChange[i]
              right -= tempChange[i-1]
              max_change = max(max_change, max(left, right))
          return max_change



'''
public long getMaxAggregateTemperatureChange(int[] tempChange) {
        int n = tempChange.length;
        long[] prefixSums = new long[n];
        long[] suffixSums = new long[n];
        
        // Compute prefix sums
        prefixSums[0] = tempChange[0];
        for (int i = 1; i < n; i++) {
            prefixSums[i] = prefixSums[i - 1] + tempChange[i];
        }
        
        // Compute suffix sums
        suffixSums[n - 1] = tempChange[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixSums[i] = suffixSums[i + 1] + tempChange[i];
        }
        
        // Find maximum aggregate temperature change
        long maxAggregateChange = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            long maxChange = Math.max(prefixSums[i], suffixSums[i]);
            maxAggregateChange = Math.max(maxAggregateChange, maxChange);
        }
        
        return maxAggregateChange;
}
'''