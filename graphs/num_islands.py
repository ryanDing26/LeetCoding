from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Level: Medium

        Problem Statement
        -----------------
        Given a 2D grid grid where '1' represents land and '0' represents
        water, count and return the number of islands.

        An island is formed by connecting adjacent lands horizontally or
        vertically and is surrounded by water. You may assume water is
        surrounding the grid (i.e., all the edges are water).

        Approach
        --------
        1. Keep track of all the grid points you have visited and a counter for
           the number of islands there are.
        2. Run DFS on each of the grid points, assuming that they have not yet
           been visited, incrementing the number of islands each time.
        2a. In DFS, you want to check adjacent islands, but not increment the 
            islands counter because you are still on the same island, you just
            want to keep track of the visited grid points. 

        TC/SC
        -----
        TC: 
        SC: O(n) 
        '''
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or (r,c) in visited:
                return
            visited.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                dfs(r + dr,  c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)

        return islands