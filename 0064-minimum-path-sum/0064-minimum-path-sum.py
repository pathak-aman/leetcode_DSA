class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Greedy fails -> No uniformity
        # Recursion

        # f(i,j) -> Minimum path sum from 0,0 to i,j
        # f(m-1, n-1) -> Our target

        # 1. Recursion - Top dowm

        # def f(i,j):
        #     # Base cases
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     if i < 0 or j < 0:
        #         return float('inf')
        
        #     up = grid[i][j] + f(i-1,j)
        #     left = grid[i][j] + f(i,j-1)

        #     return min(up, left)
    
        # m = len(grid)
        # n = len(grid[0])
        # return f(m-1, n-1)

        # TC: O(2^mn)
        # SC: O((m-1) + (n-1))

        # 2. Using DP

        # def f(i,j):
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     if i < 0 or j < 0:
        #         return float('inf')
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     left = grid[i][j] + f(i-1,j)
        #     up = grid[i][j] + f(i,j-1)

        #     dp[i][j] = min(left, up)

        #     return dp[i][j]

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1 for _ in range(n)] for _ in range (m)]
        # return f(m-1, n-1)

        # TC: O(m*n)
        # SC: O((m-1) + (n-1)) + O(m*n)

        # 3. Tabulation (bottom up)
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range (m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                    continue
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                else:
                    left = float('inf')
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                else:
                    up = float('inf')
                
                dp[i][j] = min(left, up)
        # print(dp)
        return dp[m-1][n-1]

        # TC: O(m*n)
        # SC: O(m*n)
        


        



