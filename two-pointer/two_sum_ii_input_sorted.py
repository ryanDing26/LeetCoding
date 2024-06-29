from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given an array of integers numbers that is sorted in non-decreasing 
        order.

        Return the indices (1-indexed) of two numbers, [index1, index2], such 
        that they add up to a given target number target and index1 < index2. 
        Note that index1 and index2 cannot be equal, therefore you may not use 
        the same element twice.

        Approach
        --------
        1. Initialize a left and right pointer to the ends of the array.
        2. While the left pointer is to the left of the right pointer, check to
           see what value the sum of values at the indices of the left and
           right pointer make. If it is the target, return the left and right
           indices with a plus 1 to account for 1-indexing. If the sum is 
           greater than the target, move the right pointer inward by 1 index. 
           If the sum is less than the target, move the left pointer inward by
           1 index.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1