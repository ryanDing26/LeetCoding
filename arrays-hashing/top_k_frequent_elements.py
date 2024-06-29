from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given an integer array nums and an integer k, return the k most 
        frequent elements within the array.

        The test cases are generated such that the answer is always unique.

        You may return the output in any order.
        
        Approach
        --------
        1. Keep track of the counts of all values in the array with a dict.
        2. Create a bucket of size n + 1, where index i represents a
           frequency of a number and the values are in the list frequencies[i]
        3. Go through the dict in step 1, and the keys to the lists at the
           index of the value.
        4. Iterate over the frequencies array, appending elements to the answer
           array until the answer array is the same length as k.

        Explanation
        -----------
        This is a modified version of bucket sort; you will only ever see an 
        element a maximum of len(nums) times, so you only need that many 
        buckets + 1 to each represent element frequencies (Python's 0 indexing 
        means the bucket at index 0 does go unused). As a result, you can go
        through the frequency buckets backwards to get the elements that show
        up most to least frequent until you get the top k frequent elements.


        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        answer = []

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for key, value in counts.items():
            frequencies[value].append(key)
        
        for i in range(len(frequencies) - 1, 0, -1):
            for element in frequencies[i]:
                answer.append(element)
                if len(answer) == k:
                    return answer