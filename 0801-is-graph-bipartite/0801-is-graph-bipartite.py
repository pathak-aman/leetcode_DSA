from queue import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # We will try to color the nodes. 
        n = len(graph)
        visited = [0 for i in range(n)]
        color = [0 for i in range(n)]
        # Two colours = 1 and -1
        # 0 -> uncolored

        # Traverse using bfs
        def bfs_bipartite(start, visited, color, graph):
            visited[start] = 1
            q = deque([start])

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for conn in graph[node]:

                        if not visited[conn]:
                            visited[conn] = 1
                            color[conn] = -1 * color[node]
                            q.append(conn)

                        elif color[conn] == color[node]:
                            return False
            return True


        # Traverse on all nodes
        for i in range(n):
            if visited[i] == 0 and color[i] == 0:
                visited[i] = 1
                color[i] = 1
                if bfs_bipartite(i, visited, color, graph):
                    continue
                else:
                    return False

        return True

