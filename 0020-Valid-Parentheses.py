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

# Solution using Stack

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif not stack or brackets[stack.pop()] != bracket:
                return False
        return not stack