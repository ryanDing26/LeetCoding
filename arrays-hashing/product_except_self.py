from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Level: Medium
        
        Problem Statement
        -----------------
        Given an integer array nums, return an array output where output[i] is 
        the product of all the elements of nums except nums[i].

        Approach
        --------
        1. Keep a prefix and postfix product counter to get the product of all 
           numbers directly before and directly after the "self".
        2. Make a result array the size of the input array for the products.
        3. For each index in the first pass (to store the prefix products), 
           Set the value at the index to be the running prefix value (if there
           was no value prior, then it is just 1). Then, after storing the
           value, multiply the running prefix number by the current value at 
           the same index in the input array.
        4. Repeat this process, but backwards and with a postfix number;
           additionally, instead of simply setting the value at the index in
           the output array to the running postfix number, multiply it by the
           running postfix number and update it in a similar manner as detailed
           in Step 3.

        TC/SC
        -----
        TC: O(n)
        SC: O(1) (result array does not count)
        '''
        prefix, postfix = 1, 1

        products = [1] * len(nums)
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        
        return products