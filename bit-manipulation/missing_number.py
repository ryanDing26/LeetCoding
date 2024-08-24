from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given an array nums containing n integers in the range [0, n] without
        any duplicates, return the single number in the range that is missing
        from nums.

        Approach
        --------
        1. Given that we know the sum of numbers from 0 to n is n*(n + 1) / 2,
           that will be the expected sum of our array.
        2. We can also sum up the nums array that we currently have, and in
           taking the difference between the two array sums, every value should
           cancel out besides the one that is missing in nums.

        TC/SC
        -----
        TC: O(1)
        SC: O(1)
        '''
        return (len(nums)*(len(nums)+1) // 2) - sum(nums)
