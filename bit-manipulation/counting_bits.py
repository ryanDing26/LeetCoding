from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

        Return an array output where output[i] is the number of 1's in the binary representation of i.

        Approach
        --------
        Commented out approach: O(ones*n)

        Other approach: DP; O(n)
        TC/SC
        -----
        TC: 
        SC: 
        '''
        
        output = []
        for i in range(n+1):
            ones = 0
            while i:
                i = i & (i-1)
                ones += 1
            output.append(ones)

        return output