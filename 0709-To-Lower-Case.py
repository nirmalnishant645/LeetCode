'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str])
