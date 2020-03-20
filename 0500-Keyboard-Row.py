'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

 

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key_rows = {'q' : 1, 'w' : 1, 'e' : 1, 'r' : 1, 't' : 1, 'y' : 1, 'u' : 1, 'i' : 1, 'p' : 1, 'o' : 1, 'a' : 2, 's' : 2, 'd' : 2, 'f' : 2, 'g' : 2, 'h' : 2, 'j' : 2, 'k' : 2, 'l' : 2,
                   'z' : 3, 'x' : 3, 'c' : 3, 'v' : 3, 'b' : 3, 'n' : 3, 'm' : 3}
        res = []
    
        for word in words:
            row, flag = key_rows[word[0].lower()], True
            for letter in word:
                if key_rows[letter.lower()] != row:
                    flag = False
                    break
            if flag:
                res.append(word)
        
        return res
