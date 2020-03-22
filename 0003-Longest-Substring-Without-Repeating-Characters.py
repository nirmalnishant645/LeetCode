'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        ch = {}
        
        for i, c in enumerate(s):
            if c in ch and start <= ch[c]:
                start = ch[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
                
            ch[c] = i
            
        return max_len
