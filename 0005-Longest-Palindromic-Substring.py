'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = end = 0
        
        for i in range(len(s)):
            length = self.expand_from_mid(s, i, i)
            length1 = self.expand_from_mid(s, i, i + 1)
            length = max(length, length1)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start : end + 1]
        
    def expand_from_mid(self, s, left, right):
        
        while left >= 0 and right <  len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1