from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given an integer n, count the number of 1's in the binary 
        representation of every number in the range [0, n].

        Return an array output where output[i] is the number of 1's in the
        binary representation of i.
        
        Approach
        --------
        1. Initialize an output array of size n + 1, and an offset of 1.
        2. Loop through every number from 1 to n  

        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        # Working solution based on Number of 1 Bits solution
        # output = []
        # for i in range(n+1):
        #     ones = 0
        #     while i:
        #         i = i & (i-1)
        #         ones += 1
        #     output.append(ones)

        # return output

        # Better solution!
        output = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            output[i] = 1 + output[i - offset]
        
        return output