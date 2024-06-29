from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Level: Medium
        
        Problem Statement
        -----------------
        Given an array of strings strs, group all anagrams together into 
        sublists. You may return the output in any order.

        An anagram is a string that contains the exact same characters as 
        another string, but the order of the characters can be different.

        Approach
        --------
        1. Create a dictionary to store results for later
        2. Add each string in sorted alphabetical order into the dictionary 
           as a key and map it to an empty array.
        3. Get each string sorted again, but append their original, unsorted
           state into the array value with the key of their sorted string.
        4. Do another pass through the array and append each array result into
           the final grouped anagram array output.
        '''
        strings = {}
        anagrams = []

        for string in strs:
            strings[str(sorted(string))] = []
        
        for string in strs:
            strings[str(sorted(string))].append(string)

        
        for key in strings:
            anagrams.append(strings[key])

        return anagrams