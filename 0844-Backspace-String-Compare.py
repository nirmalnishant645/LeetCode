'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        backS, upperS, backT, upperT = 0, len(S) - 1, 0, len(T) - 1
        while True:
            while upperS >= 0 and (backS or S[upperS] == '#'):
                backS += 1 if S[upperS] == '#' else -1
                upperS -= 1
            while upperT >= 0 and (backT or T[upperT] == '#'):
                backT += 1 if T[upperT] == '#' else -1
                upperT -= 1
            if not (upperS >= 0 and upperT >= 0 and S[upperS] == T[upperT]):
                return upperS == upperT == -1
            upperS, upperT = upperS - 1, upperT - 1

