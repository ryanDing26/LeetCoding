from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given an array of integers nums, find the subarray with the largest sum and return the sum.

        A subarray is a contiguous non-empty sequence of elements within an array.
        Approach
        --------
        1. Keep a running counter of the current subarray sum as well as the max subarray sum, set to 0 and the first value of the nums subarray respectively.
        2. Iterate over each value in the array, check if the sum leading up to the value is negative. If it is, then reset the current sum to be 0 as adding a negative
           prefix to your subarray will cause its value to go down, add the current value in the subarray it is on, and constantly update the maximum subarray value you have by
           comparing that running current sum and the current max subarray value stored in the variable.
        3. Return whatever is stored in the maximum subarray value variable at the end of the loop.

        TC/SC
        -----
        TC: O(n) 
        SC: O(1)
        '''
        max_val = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_val = max(max_val, cur_sum)

        return max_val