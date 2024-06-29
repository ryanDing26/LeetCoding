from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given an integer array nums, return all the triplets [nums[i], nums[j],
        nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j 
        and k are all distinct.

        The output should not contain any duplicate triplets. You may return 
        the output and the triplets in any order.

        Approach
        --------
        1. Sort the input array and initialize a triplets output array.
        2. Enumerate over an index and keep track of whether or not (a) the
           value is nonpositive (if it is, then we can end the loop) or (b) the
           value is the same as the one prior to it, e.g. a duplicate value (if
           it is, then we just skip over the value).
        3. Set some left and right pointer to be the array one index after the
           index set in Step 2 and the end of the array respectively. Perform a
           similar check to to that of two_sum_ii_input_sorted.py, moving the
           left pointer in if the sum is less than 0 and the right pointer in
           if the sum is greater than 0.
        4. If the sum is equal to one, append the values at the three i, l,
           and r indices whilst also moving the both left and right pointers
           one spot inwards. However, check if moving one of the pointers
           inwards results in the same value as before; if it does, just skip
           over that value as well until you see a new value (this is done via
           the left pointer in the code, but can be done with the right pointer
           as well).

        TC/SC
        -----
        TC: O(n^2)
        SC: O(1) - O(n) depending on if sorting nums takes extra memory per 
            libraries used
        '''
        nums = sorted(nums)
        triplets = []
        for i, nonpos in enumerate(nums):
            if nonpos > 0:
                break
            if i > 0 and nonpos == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets.append([nonpos, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return triplets