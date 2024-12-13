from collections import defaultdict
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        first_index = {}
        last_index = {}
        listofsub = []
        
        for i in range(len(nums)):
            num = nums[i]
            frequency[num] += 1
            if num not in first_index:
                first_index[num] = i
            last_index[num] = i
        
        
        max_freq = max(frequency.values())
        
        for num, freq in frequency.items():
            if freq == max_freq:
                length = last_index[num] - first_index[num] + 1
                listofsub.append(length)
        
       
        return min(listofsub)
