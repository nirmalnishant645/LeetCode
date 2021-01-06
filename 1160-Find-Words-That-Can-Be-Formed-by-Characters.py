'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
'''

# Method 1 using List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_counts = [0] * 26
        
        for char in chars:
            char_counts[ord(char) - ord('a')] += 1
            
        for word in words:
            temp = list(char_counts)
            valid_char_count = 0
            
            for char in word:
                if temp[ord(char) - ord('a')]:
                    valid_char_count += 1
                    temp[ord(char) - ord('a')] -= 1
                    
            if valid_char_count == len(word):
                res += valid_char_count
        
        return res

# Method 2 using HashTable

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        for char in chars:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        res = 0
        for word in words:
            summ = 0
            temp = chars_dict.copy()
            for char in word:
                if char in temp and temp[char]:
                    temp[char] -= 1
                    summ += 1
            if summ == len(word):
                res += summ
        return res