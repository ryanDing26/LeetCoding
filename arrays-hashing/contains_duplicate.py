from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given an integer array nums, return true if any value appears more
        than once in the array, otherwise return false.


        Approach
        --------
        1. Check that the making a set from the array results in the same
           length as the original array (meaning no duplicates since set 
           duplicates only appear once).
        '''
        return len(set(nums)) != len(nums)
