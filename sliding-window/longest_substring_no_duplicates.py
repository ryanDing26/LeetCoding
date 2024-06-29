class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given a string s, find the length of the longest substring without 
        duplicate characters.

        A substring is a contiguous sequence of characters within a string.

        Approach
        --------
        1. Initialize a set to keep track of the letters in a substring, a
           longest length counter to constantly update, and a left pointer.
        2. Iterate over the characters in the string (using the iterator as a 
           sort of right pointer), and if the character at the right pointer is
           already in the subtring letter set, remove the character at the left
           substring and increment the left pointer by one, until the character
           at the right pointer is no longer in the set.
        3. After the conditions have been met, place the character at the right
           pointer into the substring letter set and update the longest length
           counter to be the maximum between what it currently is, and your
           current substring window without duplicates.
        4. After iterating over the entire string, return the longest length
           counter.

        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        substr_letters = set()
        length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in substr_letters:
                substr_letters.remove(s[l])
                l+= 1
            substr_letters.add(s[r])
            length = max(length, r - l + 1)
        return length