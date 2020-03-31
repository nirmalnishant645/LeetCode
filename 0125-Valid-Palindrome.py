'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1
        
        while first < last:
            
            if not s[first].isalnum():
                first += 1
                continue
            
            elif not s[last].isalnum():
                last -= 1
                continue
            
            elif s[first].lower() != s[last].lower():
                return False
            
            first += 1
            last -= 1
        
        return True
