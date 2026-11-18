# Intuition - we use Dijistka's to keep track of the path with minimum effort. In a heap queue, we traverse by popping minimum effort.
# We stop when the popped element is the destination, as no more path will have lower effort (same or higher only)

import heapq
from math import inf

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        efforts = [[inf for _ in range(m)] for _ in range(n)]
        min_heap = []
        # (effort, (x,y))
        heapq.heappush(min_heap, (0, (0,0)))

        delx = [0, 1, 0, -1]
        dely = [1, 0, -1 ,0]

        while min_heap:
            curr_effort, (x,y) = heapq.heappop(min_heap)
            if (x,y) == (n-1, m-1):
                return curr_effort

            for dx, dy in zip(delx, dely):
                x_new, y_new = x+dx, y + dy

                # validity check:
                if 0 <= x_new < n and 0 <= y_new < m and max(curr_effort, abs(heights[x][y] - heights[x_new][y_new])) < efforts[x_new][y_new]:
                    new_effort = max(curr_effort, abs(heights[x][y] - heights[x_new][y_new]))
                    efforts[x_new][y_new] =  new_effort
                    heapq.heappush(min_heap, (new_effort, (x_new, y_new)))