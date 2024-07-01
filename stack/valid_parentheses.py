class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Level: Easy

        Problem Statement
        -----------------
        You are given a string s consisting of the following characters: '(', 
        ')', '{', '}', '[' and ']'.

        The input string s is valid if and only if:

        1. Every open bracket is closed by the same type of close bracket.
        2. Open brackets are closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same 
           type.

        Return true if s is a valid string, and false otherwise.

        Approach
        --------
        1. Initialize a stack and a parentheses dictionary, with closing 
           parentheses mapping to opening parentheses.
        2. Iterate over the string; if you encounter an open parentheses, push 
           it onto the stack. If you encounter a closing parentheses, first 
           check if there is anything on the stack, then check if the top of 
           the stack's opening parentheses matches the closing parentheses. If
           not, return False. If it does, pop the parentheses at the top of the
           stack.
        3. If you iterated over the whole string without returning False early,
           check if the stack is empty. If not, that means that not all 
           parentheses were closed (return False). If it is, return True.
           
        TC/SC
        -----
        TC: O(n)
        SC: O(n)
        '''
        stack = []
        parentheses = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in parentheses:
                if not stack or parentheses[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack