'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 

Constraints:

    1 <= text.length <= 10^4
    text consists of lower case English letters only.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b' : 0, 'a' : 0, 'l' : 0, 'o' : 0, 'n' : 0}
        for i in text:
            if i in d:
                d[i] = d.get(i, 0) + 1
        d['l'], d['o'] = d.get('l', 0) // 2, d.get('o', 0) // 2
        least = d['b']
        for alpha, count in d.items():
            least = count if count < least else least
        return least
