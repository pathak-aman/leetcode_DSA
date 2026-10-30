class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Count connected components. 
        m,n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # Traversal - DFS

        def dfs(i,j, visited, grid):
            delta_x = [1,0,-1,0]
            delta_y = [0,-1,0,1]
            visited[i][j] = 1

            for dx, dy in zip(delta_x, delta_y):
                x = i + dx
                y = j + dy

                if 0 <= x < m and 0 <= y <n and grid[x][y] == '1' and not visited[x][y]:
                    visited[x][y] = 1
                    dfs(x,y, visited, grid)

        islands = 0
        # Initiate the traversal on the visited array.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands += 1
                    visited[i][j] = 1
                    dfs(i,j, visited, grid)
        
        return islands


        