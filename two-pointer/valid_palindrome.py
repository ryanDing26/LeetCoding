class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given a string s, return true if it is a palindrome, otherwise return 
        false.

        A palindrome is a string that reads the same forward and backward. It 
        is also case-insensitive and ignores all non-alphanumeric characters.

        Approach
        --------
        1. Remove all non-alphanumeric characters from the string and convert
           all letters to lowercase
        2. Set a left and right pointer to both ends of the string
        3. While the left pointer is to the left of the right pointer, continue
           to check if the characters at the left and right pointer values are
           the same. If not, return False. If they are, move both pointers
           inward by one character.
        4. If you get through the loop, then your string is a palindrome.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        s = ''.join(char.lower() for char in s if char.isalnum())
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True