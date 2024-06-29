class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Level: Easy
        
        Problem Statement
        -----------------
        Given two strings s and t, return true if the two strings are anagrams
        of each other, otherwise return false.

        An anagram is a string that contains the exact same characters as 
        another string, but the order of the characters can be different.

        Approach
        --------
        1. Sort both strings and see if they are the same string then.
        '''
        return sorted(s) == sorted(t)