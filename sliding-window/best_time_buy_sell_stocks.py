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
        1. Set the lowest prices value to the first in the list and the current
           best profit to 0.
        2. Iterate over the prices array and if you find some lower price than
           the current lowest price (to serve as a buying price), update
           lowest and constantly check if selling on that day would lead to the
           highest value profit. Repeat until end of loop.
        3. Return max profit value gained in the profit variable.

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