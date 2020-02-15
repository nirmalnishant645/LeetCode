'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set()
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        string = list(s)
        start, end = 0, len(s) - 1
        while start <= end:
            if string[start] in vowels:
                if string[end] in vowels:
                    string[start], string[end] = string[end], string[start]
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        return ''.join(string)
