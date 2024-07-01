class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Run loop as many times as there are ones in the loops.

        n & (n - 1) essentially "counts" a 1 bit inside n and for each iteration whilst n is not all 0s, counts the ones inside of it. This is better and would take O(ones), upper bounded by O(32)

        Another way would be to mod 2 the value and continue to right shift it until it is not 0, which takes O(32) time consistently.
        '''
        ones = 0
        while n:
            n = n & (n-1)
            ones += 1
        return ones