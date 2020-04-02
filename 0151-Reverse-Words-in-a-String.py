'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        self.reverseWord(s, 0, len(s) - 1)
        start = i = 0
        while i < len(s):
          if s[i] != ' ':
            if start != 0:
              s[start] = ' '
              start += 1
            j = i
            while j < len(s) and s[j] != ' ':
              s[start] = s[j]
              j += 1
              start += 1
            self.reverseWord(s, start - (j - i), start - 1)
            i = j
          i += 1
        return ''.join(s[:start])
    
    def reverseWord(self, s, start, end):
        while start < end:
          s[start], s[end] = s[end], s[start]
          start += 1
          end -= 1
