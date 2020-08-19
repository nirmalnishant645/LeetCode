'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        
        for idx, word in enumerate(s):
            
            s[idx] = ''.join(self.reverse(list(word)))  
            
        return " ".join(s)
            
    def reverse(self, word):
        
        start = 0
        end = len(word) - 1;
        
        while start < end:
            
            word[start], word[end] = word[end], word[start]
            
            start += 1
            end -= 1
            
        return word