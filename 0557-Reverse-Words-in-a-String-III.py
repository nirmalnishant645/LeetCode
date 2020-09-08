'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution:
    def reverseWords(self, s: str) -> str:    
        s = list(s)
        start = 0
        
        for i, let in enumerate(s):
            if let == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
            if i == len(s) - 1:
                self.reverse(s, start, i)
            
        return ''.join(s)
            
    def reverse(self, word, start, end):
        
        while start < end:
            
            word[start], word[end] = word[end], word[start]
            
            start += 1
            end -= 1