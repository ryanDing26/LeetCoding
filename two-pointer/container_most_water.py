from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        You are given an integer array heights where heights[i] represents the 
        height of the i^{th} bar.

        You may choose any two bars to form a container. Return the maximum 
        amount of water a container can store.

        Approach
        --------
        1. Set left and right pointers to ends of heights array.
        2. Keep updating the area to be the maximum of what it is currently and
           what it is based on the pointer locations (explained further below)
        3. When the left pointer is no longer the left pointer, return the area
           you kept updating

        Step 2 Explained: your container can fit as much water as the lesser of
        the two heights, hence why min(heights[l], heights[r]) is taken. The
        width of the container would be the difference in index between the two
        pointers.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area