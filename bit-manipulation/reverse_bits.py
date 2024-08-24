class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given a 32-bit unsigned integer n, reverse the bits of the binary
        representation of n and return the result.
        
        Approach
        --------
        1. Set a new result variable equal to 0.
        2. For each bit, starting from the rightmost side of the 32-bit number,
           mask it with a 1 such that you are able to extract its value of True
           (1) or False (0) into another variable, bit.
        3. Add this new bit value to the front of the result variable with a
           left shift of 32 - i, the current number of bits from the rightmost
           bit that you are on.
        4. Return the resulting bit after all 32-bits have been masked and
           added.

        TC/SC
        -----
        TC: O(32) or O(1)
        SC: O(32) or O(1)
        '''
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res