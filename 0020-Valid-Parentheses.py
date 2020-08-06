'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {')' : '(', ']' : '[', '}' : '{'}
        
        stack = []
        
        if len(s) % 2:
            return False
        
        for paren in s:
            
            if paren in parentheses.values():
                stack.append(paren)
            
            elif not stack or parentheses[paren] != stack.pop():
                return False
            
        return not stack