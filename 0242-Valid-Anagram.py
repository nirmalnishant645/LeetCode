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
        
        check = {}
        
        for letter in s:
            
            check[letter] = check.get(letter, 0) + 1
                
        for letter in t:
            
            if check.get(letter, 0) <= 0:
                return False
            check[letter] -= 1
            
        return True