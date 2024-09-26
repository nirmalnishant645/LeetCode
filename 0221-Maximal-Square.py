'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0]) if len(matrix) else 0
        length = [0] * (cols + 1)
        max_len = prev = 0
        
        for i in range(1, rows + 1):
            
            for j in range(1, cols + 1):
                
                temp = length[j]
                
                if matrix[i - 1][j - 1] == '1':
                    
                    if length[j - 1] < prev:
                        length[j] = length[j - 1] if length[j - 1] < length[j] else length[j]
                    
                    else:
                        length[j] = prev if prev < length[j] else length[j]
                    
                    length[j] += 1
                    max_len = length[j] if length[j] > max_len else max_len
                
                else: length[j] = 0
                
                prev = temp
        
        return max_len * max_len
