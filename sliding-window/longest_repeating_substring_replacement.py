class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        You are given a string s consisting of only uppercase english
        characters and an integer k. You can choose up to k characters of the
        string and replace them with any other uppercase English character.

        After performing at most k replacements, return the length of the
        longest substring which contains only one distinct character.

        Approach
        --------
        1. Set the left pointer to the beginning of the string, and the right
           pointer to iterate over the string itself
        2. Keep track of the letter of maximum frequency within the window of
           substring you are checking over.
        3. If it is ever the case that the difference between the length of the
           window covered by the right and left pointer and the character with
           the maximum frequency becomes greater than the number of character
           replacements you can do (k), shift over the left window to the right
           by one character and update the character frequency dictionary
           accordingly.
        4. Return the length of the window after the iteration is finished. 

        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        l = 0
        max_frequency = 0
        frequency = dict()
        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            max_frequency = max(max_frequency, frequency[s[r]])
            if (r - l + 1) - max_frequency > k:
                frequency[s[l]] -= 1
                l += 1
        
        return (r - l + 1)