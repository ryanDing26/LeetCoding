from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Level: Easy
        
        Problem Statement
        -----------------
        
        Approach
        --------
        1. Keep a dictionary of value already seen in the array with values
           mapping to their indices (since we want indices)
        2. For each value in the array, get the remaining amount needed for the
           target value, described as the target minus the current value.
        3. If you can find the current value as a key in the dictionary in step
           1, return the value at seen[current value] and the current index.
        4. If not, add the value you just saw into the dictionary as 
           {value: index}.
        '''
        seen = {}

        for i, num in nums:
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
            