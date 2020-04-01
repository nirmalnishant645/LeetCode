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
        l, m, x = len(s) , 0, 0
        for i in range(l):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < l and s[a] == s[b]:
                    a -= 1
                    b += 1
                    if b - a - 1 > m:
                        m, x = b - a - 1, a + 1
        return s[x : x + m]
