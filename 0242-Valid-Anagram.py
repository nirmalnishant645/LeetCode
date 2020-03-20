'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        
        for c in s:
            letters[c] = 1 if c not in letters else letters[c] + 1
            
        for c in t:
            if c not in letters or not letters[c]:
                return False
            letters[c] -= 1
            
        return True
