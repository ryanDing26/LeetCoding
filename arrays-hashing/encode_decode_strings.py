from typing import List

class Solution:
    '''
    Level: Medium
    
    Problem Statement
    -----------------
    Design an algorithm to encode a list of strings to a single string. The 
    encoded string is then decoded back to the original list of strings.
    
    Approach
    --------
    ENCODE
    1. Encode a list of strings as such: [length of string][delimiter][string]
       In this algorithm, the delimiter is a # symbol.

    DECODE
    1. Take the encoded string and find the index that the delimiter is at.
    2. Slice the string from the beginning up until the index of the delimiter
       to get the length of the next string and store that.
    3. Append the decoded string by slicing the encoded string from the index
       right after the delimiter ("i + 1") until the index after the delimiter
       plus the length of the string ("char", "i + 1 + length").
    4. Set the "#" finder equal to the character right after the end of the
       string, which should be at an integer.
    5. Repeat until your index finder is greater than or equal to the length of
       the encoded string.

    Added Note
    ----------
    This is how serialization algorithms work if I ever end up tutoring CSE 100
    again.

    TC/SC
    -----
    TC: O(n)
    SC: O(n)
    '''
    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            encoding += f"{len(string)}#{string}"

        return encoding

    def decode(self, s: str) -> List[str]:
        decoding = []
        i = 0
        while i < len(s):
            char = i
            while s[char] != "#":
                char += 1
            length = int(s[i:char])
            i = char + 1 # Character right after "#"
            char = i + length # String up until next integer
            decoding.append(s[i:char])
            i = char # The next integer to read in
        return decoding