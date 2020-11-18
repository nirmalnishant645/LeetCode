'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h, v  = len(grid), len(grid[0])
        res = 0

        for i in range(h):
            for j in range(v):
                if grid[i][j]:
                    res += 4
                    if i < h - 1 and grid[i + 1][j]:
                        res -= 2
                    if j < v - 1 and grid[i][j + 1]:
                        res -= 2

        return res
