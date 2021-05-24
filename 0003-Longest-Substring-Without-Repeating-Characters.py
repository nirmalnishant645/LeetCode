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

from typing import List

# Two Pointers and Hash Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxx = 0
        
        char = set()
        
        while right < len(s):
            if s[right] in char:
                char.remove(s[left])
                left += 1
            else:
                char.add(s[right])
                right += 1
                maxx = max(len(char), maxx)
        
        return maxx

# Two Pointers and Hash Table

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_len = 0
        d = {}
        while left < len(s) and right < len(s):
            if s[right] in d:
                left = max(left, d[s[right]] + 1)
            d[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

# Custom Input Check

s = Solution()
answer = s.lengthOfLongestSubstring("nishant") # 6
print(answer)