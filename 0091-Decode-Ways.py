'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        prev_no_of_ways = 0
        no_of_ways = int(s > '')
        prev_digit = ''
        
        for digit in s:
            copy_prev = prev_no_of_ways
            prev_no_of_ways = no_of_ways
            
            no_of_ways = (digit > '0') * no_of_ways
            
            no_of_ways += (9 < int(prev_digit + digit) < 27) * copy_prev
            
            prev_digit = digit
            
        return no_of_ways
