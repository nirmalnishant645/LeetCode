'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution:
    def reverseWords(self, s: str) -> str:    
        res = []
        word = ""
        
        for i, let in enumerate(s):
            if let == ' ' or i == len(s) - 1:
                if i == len(s) - 1:
                    word += let
                res.append(self.reverse(list(word)))
                word = ""
            else:
                word += let
            
        return ' '.join(res)
            
    def reverse(self, word):
        
        start = 0
        end = len(word) - 1;
        
        while start < end:
            
            word[start], word[end] = word[end], word[start]
            
            start += 1
            end -= 1
            
        return ''.join(word)