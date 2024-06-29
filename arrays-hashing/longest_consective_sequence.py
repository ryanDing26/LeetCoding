from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given an array of integers nums, return the length of the longest 
        consecutive sequence of elements.

        A consecutive sequence is a sequence of elements in which each element
        is exactly 1 greater than the previous element.
        
        Approach
        --------
        1. Convert the input array to a set and initialize some longest counter
           to return later.
        2. Go through the set and if there is some value that is one less than
           the current number in the iteration, don't do anything (explained
           below).
        3. If the value - 1 is not in the set, then initialize some other
           variable to capture the current sequence length and keep trying to
           find the next number in the sequence in the set, incrementing the
           counter every time you find one.
        4. Once you cannot find value + 1 in the set, update your longest
           counter to be the maximum between what it is currently and the most
           recent sequence length you captured.
        5. Return the longest counter after iterating through the entire set.

        Explanation for Step 2: Since we want to find the length of a sequence
        in its entirety, it would not make sense to start in the middle of a
        sequence. If value - 1 is in the set, then that means that you are not
        at the beginning of a sequence and should not perform the rest of the
        algorithm at the time, instead opting for when you are at a value that
        can serve as the first number in a sequence, which does not have value
        - 1 in the set.
        
        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if (num - 1) not in set_nums:
                length = 1
                while (num + length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest

