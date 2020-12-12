'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

# Using Backtracking

class Solution:
    
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    
    def search(self, board, word, m, n, cur):
        if m < 0 or m >= len(board) or n < 0 or n >= len(board[m]) or board[m][n] == '':
            return False
        
        cur += board[m][n]
        
        if len(cur) > len(word):
            return False
        if cur[len(cur)-1] != word[len(cur)-1]:
            return False
        if cur == word:
            return True
        
        temp, board[m][n] = board[m][n], ''
        
        for i in range(4):
            if self.search(board, word, m+self.x[i], n+self.y[i], cur):
                return True
        board[m][n] = temp
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        for i in range(len(board)):
            for  j in range(len(board[i])):
                if board[i][j] ==  word[0] and self.search(board, word, i, j, ''):
                    return True
        return False