from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Level: Easy

        Problem Statement
        -----------------
        You are given an integer array prices where prices[i] is the price of a
        stock on the i^{th} day.

        You may choose a single day to buy one stock and choose a different 
        day in the future to sell it.

        Return the maximum profit you can achieve. You may choose to not make 
        any transactions, in which case the profit would be 0.

        Approach
        --------
        1. Set the lowest

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        lowest = prices[0]
        profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)

        return profit