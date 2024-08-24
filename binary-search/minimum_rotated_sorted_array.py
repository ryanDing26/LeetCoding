from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        You are given an array of length n which was originally sorted in
        ascending order. It has now been rotated between 1 and n times. For
        example, the array nums = [1,2,3,4,5,6] might become:

        [3,4,5,6,1,2] if it was rotated 4 times.
        [1,2,3,4,5,6] if it was rotated 6 times.

        Assuming all elements in the rotated sorted array nums are unique,
        return the minimum element of this array.

        Approach
        --------
        1. Set a left/right or start/end pointer and a minimum result tracker.
        2. Whilst the two pointers do not overlap, find the midpoint value in
           the current array between the start and end pointers, and update
           your stored minimum value to be either this new middle value or the
           current value stored.
        3. If the middle value is greater than the value at the end, this means
           that we want to search the right side of the rotated array to find
           the minimum value. Otherwise, we want to search the left side of the
           rotated array, all until the two pointers overlap with one another.
        4. Return the minimum value between the current left/starting pointer
           of the rotated array and the current minimum value stored.

        Further Explanation: in an array like [3,4,5,1,2], the comparison would
        perform 5 > 2, which is true. What this means is that the array was
        rotated so much that the minimum value, which would have originally
        been in the left half/start of the array, was rotated so many times
        that it got put into the right half of the array, hence why we adjust
        the starting pointer to check the second half of the array instead. The
        opposite holds true on why we decide to search the left half of the
        array if that is not the case.

        Note: curr_min is initialized to 1001 because one condition was that
        -1000 <= nums[i] <= 1000.
        
        TC/SC
        -----
        TC: O(logn)
        SC: O(1)
        '''
        start, end = 0, len(nums) - 1
        curr_min = 1001
        while start < end:
            middle = start + (end - start) // 2
            curr_min = min(curr_min, nums[middle])

            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle - 1
        
        return min(curr_min, nums[start])