from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited_arr = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()
        fresh_oranges = 0

        # Search fopr all rotten oranges -> O(mn)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited_arr[i][j] = 1
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        def bfs(q, visisted_arr, fresh_oranges):
            time = -1
            delta_x = [0, 1, 0, -1]
            delta_y = [1, 0, -1, 0]

            # Do bfs
            
            while len(q):
                time += 1
                for _ in range(len(q)):

                    x,y = q.popleft()
                    for dx, dy in zip(delta_x, delta_y):
                        x_new, y_new = x + dx, y + dy

                        if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] == 1 and not visited_arr[x_new][y_new]:
                            visited_arr[x_new][y_new] = 1
                            fresh_oranges -= 1
                            q.append((x_new, y_new))

            if fresh_oranges:
                time = -1
            return time
        if fresh_oranges:
            return bfs(q, visited_arr, fresh_oranges)
        else:
            return 0


        